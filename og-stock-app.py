from yahooquery import Ticker
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

def invest(ticker, client=False):
    # INITIALIZE STOCK INFO
    stock = Ticker(ticker)
    sp500 = Ticker('^GSPC')

    buy = 0
    sell = 0
    hold = 0

    # FETCH SUMMARY INFO
    summary = stock.summary_detail[ticker]
    summary_sp500 = sp500.summary_detail['^GSPC']

    history = stock.history(period="1y")
    sp500_history = sp500.history(period="1y")

    summary_profile = stock.summary_profile
    stock_sector = summary_profile[ticker].get('sector')

    # Basic recommendation logic based on client type
    recommendation = 'hold'  
    explanation = ""
    explanation_parts = []

    # ARE WE IN A BEAR OR BULL MARKET
    market_sentiment = "neither"
    sp500_history['moving_average_200'] = sp500_history['adjclose'].rolling(window=200).mean()

    current_price = sp500_history['adjclose'].iloc[-1]
    moving_average_200 = sp500_history['moving_average_200'].iloc[-1]

    percentage_difference = ((current_price - moving_average_200) / moving_average_200) * 100

    if percentage_difference > 5: 
        explanation_parts.append("We are potentially in a bull market, which can be a good time to buy as markets are expected to rise further.")
        market_sentiment = "bull"
    elif percentage_difference < -5:  
        explanation_parts.append("We are potentially in a bear market, often considered a cautionary time to sell or hold off on buying as markets might decline further.")
        market_sentiment = "bear"
    else:
        explanation_parts.append("We are likely in neither a bear nor a bull market.")

    # CONSIDER THE GENERAL CASE
    # Market Capitalization Comparison
    market_cap_stock = summary['marketCap']
    if market_cap_stock > 10000000000:
        explanation_parts.append("The stock is large cap, meaning it is considered more stable and could provide steady but low returns.")
        hold += 1
    elif market_cap_stock > 2000000000:
        explanation_parts.append("The stock is medium cap, meaning it has a balance between the potential of a smaller company and the stability of a larger company.")
        buy += 1
    else:
        explanation_parts.append("The stock has a lower market cap, suggesting higher potential for growth and returns, but with higher investment risk.")
        buy += 1

    # Volatility
    history['daily_returns'] = history['close'].pct_change()
    stock_volatility = history['daily_returns'].std() * np.sqrt(252)

    sp500_history['daily_returns'] = sp500_history['close'].pct_change()
    sp500_volatility = sp500_history['daily_returns'].std() * np.sqrt(252)
    if stock_volatility > sp500_volatility:
        explanation_parts.append("The stock is more volatile than the average of the S&P 500, indicating higher risk, but also higher potential reward.")
        sell += 1
    else:
        explanation_parts.append("The stock is less volatile, suggesting a safer, more stable investment compared to the broader market.")
        hold += 1
        buy += 1

    # # Sector Performance
    sector_etf_map = {
    "Communication Services": "XLC",  
    "Consumer Cyclical": "XLY",       
    "Consumer Defensive": "XLP",      
    "Energy": "XLE",                 
    "Financial Services": "XLF",      
    "Healthcare": "XLV",              
    "Industrials": "XLI",             
    "Technology": "XLK",             
    "Basic Materials": "XLB",         
    "Real Estate": "XLRE",           
    "Utilities": "XLU"               
    }

    etf_ticker = sector_etf_map.get(stock_sector)
    etf_stock = Ticker(etf_ticker)
    etf_history = etf_stock.history(period="1y")

    stock_performance = ((history['close'].iloc[-1] - history['close'].iloc[0]) / history['close'].iloc[0]) * 100
    etf_performance = ((etf_history['close'].iloc[-1] - etf_history['close'].iloc[0]) / etf_history['close'].iloc[0]) * 100

    if stock_performance > etf_performance:
        explanation_parts.append("This stock's growth is outperforming other stocks in its same sector, which indicates competitive advantage and potential for growth.\n")
        buy += 1
    else:
        explanation_parts.append("The stock's growth is underperforming compared to other stocks in its sector, which indicates potential difficulty growing.\n")
        sell += 1
    
    # Combine the parts for the final analysis
    if client not in ('income', 'growth', 'esg'):
        if buy > sell and buy > hold:
            recommendation = 'buy'
        elif sell > buy and sell > hold:
            recommendation = 'sell'
        else:
            recommendation = 'hold'  
        explanation = " ".join(explanation_parts)
        return recommendation, explanation
    # END THE GENERAL CASE

    # Example logic for different client types, adjusted for market sentiment
    if client == 'income':
        # For income clients, prefer stocks with dividends
        dividend_yield = summary.get('dividendYield', 0)
        dividend_yield_sp500 = summary_sp500.get('dividendYield', 0)
        if dividend_yield > dividend_yield_sp500:
            recommendation = 'buy'
            explanation_parts.append("This stock has a strong recent dividend yield when compared to the SP500, making it suitable for income-focused portfolios.")
        elif market_cap_stock > 10000000000 and stock_volatility < sp500_volatility:
            recommendation = 'hold'
            explanation_parts.append("This stock shows potential for steady earnings in the future.")
        else:
            recommendation = 'sell'
            explanation_parts.append("Lack of significant dividend yield or steady growth makes this stock less suitable for income-focused portfolios.")

        five_year_dividend_avg = summary.get('fiveYearAvgDividendYield', 0)
        five_year_dividend_avg_sp500 = summary_sp500.get('fiveYearAvgDividendYield', 0)
        if five_year_dividend_avg >= five_year_dividend_avg_sp500:
            explanation_parts.append("\n Know that the five year average of dividend yields is strong. This makes it suitable in a more long-term steady approach.")
        else: 
            explanation_parts.append("The five year average of dividend yields is not strong")
            if recommendation == 'sell':
                explanation_parts.append(" either, so this makes the stock even less suitable for an income-focused portfolio.")
            elif recommendation == 'buy':
                explanation_parts.append(", however, so consider the fact that this could be a short term stock.")
            else:
                recommendation == 'sell'
                explanation_parts.append(", so this makes the stock less trustworthy when considering prior growth.")

        payout_ratio = summary.get('payoutRatio', 0)
        if payout_ratio < .35:
            explanation_parts.append("Also, the company is retaining and reinvesting a large portion of income into growth, so this could be a safer stock, but not one focused on income.")
        elif payout_ratio < .75:
            explanation_parts.append("Also, the company has a balanced approach to growth and paying dividends, so for income portfolios, this may be a good option.")
        else:
            recommendation = 'sell'
            explanation_parts.append("Finally, this company has a very high payout ratio, which means that dividends could be at risk if the company is not reinvesting into itself. This may be more of a short-term option.")
    elif client == 'growth':
        # FETCH THE 1 YEAR GROWTH RATE OF STOCK
        start_price = history['adjclose'].iloc[0] 
        end_price = history['adjclose'].iloc[-1] 
        growth_rate = ((end_price - start_price) / start_price) * 100

        # Adjust recommendations based on market sentiment and growth rate
        if market_sentiment == "bull" and summary['beta'] > 1 and growth_rate > 5:
            buy += 2
            explanation_parts.append("Given the bull market, high beta and strong growth rate, we can expect significant growth potential.")
        elif market_sentiment == "bear" and growth_rate > 0:
            buy += 1
            explanation_parts.append("Despite the bear market, this stock shows resilience with positive growth, suggesting potential for growth.")
        else:
            sell += 3
            explanation_parts.append("Limited growth potential indicated by market conditions and stock's beta or growth rate.")

        payout_ratio = summary.get('payoutRatio', 0)
        if payout_ratio < .35:
            buy += 3
            explanation_parts.append("Also, the company is retaining and reinvesting a large portion of income into growth, so this stock could exhibit a lot of growth in the coming years.")
        elif payout_ratio < .75:
            hold += 1
            explanation_parts.append("Also, the company has a balanced approach to growth and paying dividends, so this could be a safe approach if also considering income.")
        else:
            sell += 5
            explanation_parts.append("Also, this company has a very high payout ratio, which means that this may not be a good long term option if considering growth.")

        if buy > sell + hold:
            recommendation = 'buy'
            explanation_parts.append("Given the overall analysis, this stock shows strong potential for growth, aligning with a growth-focused investment strategy.")
        elif hold >= buy or hold >= sell:
            recommendation = 'hold'
            explanation_parts.append("There are mixed signals regarding the stock's growth potential, suggesting a cautious approach until clearer trends emerge.")
        else:
            recommendation = 'sell'
            explanation_parts.append("Considering the analysis, the stock may not meet the growth expectations or presents higher risks compared to potential rewards.")
        
        
    elif client == 'esg':
        # FETCH ESG SCORES OF THE STOCK
        try:
            esg_scores = getattr(stock, 'esg_scores', {}).get(ticker, {})
        except AttributeError:
            esg_scores = {}

        # Consider ESG scores in the context of market sentiment
        esg_risk_rating = esg_scores.get('totalEsg', 0)
        explanation_parts.append("Based on the average threshold for what is a safe ESG risk score, the")
        if esg_risk_rating < 25:  
            recommendation = 'buy'
            explanation_parts.append("low ESG risk score aligns with sustainable and socially responsible investing criteria.")
        else:
            recommendation = 'sell'
            explanation_parts.append("high ESG risk score suggests the company does not meet preferred ESG criteria.")

        peer_esg_risk_rating = esg_scores.get('peerEsgScorePerformance', {}).get('avg', None)
        if peer_esg_risk_rating > esg_risk_rating:
            explanation_parts.append("And, know that competitors have a higher average ESG risk score. This is certainly something to consider when making your final decision.")
        else:
            explanation_parts.append("This ESG risk score stacks well against the risk rating of competitors in the same market, which makes it even more attractive.")

        explanation_parts.append("\n\tThere are specific nuances to consider for each category of ESG, though.")

        environmental_risk_rating = esg_scores.get('environmentScore', 0)
        social_risk_rating = esg_scores.get('socialScore', 0)
        governance_risk_rating = esg_scores.get('governanceScore', 0)

        explanation_parts.append(f"First, the environmental risk score is {environmental_risk_rating}, which means")
        if environmental_risk_rating > 30:
            explanation_parts.append("the company faces high environmental risks, indicating significant concerns related to its environmental impact and sustainability practices.")
        elif environmental_risk_rating > 20:
            explanation_parts.append("the company has moderate environmental risks, suggesting some concerns that may need addressing to improve its environmental sustainability.")
        else:
            explanation_parts.append("the company is at low environmental risk, reflecting good environmental practices and minimal sustainability concerns.")

        explanation_parts.append(f"Second, the social risk score is {social_risk_rating}, which means")
        if social_risk_rating > 30:
            explanation_parts.append("the company is at high social risk, indicating serious concerns regarding social practices, human rights, labor standards, and community relations.")
        elif social_risk_rating > 20:
            explanation_parts.append("the company faces moderate social risks, with some areas for improvement in its social practices and community engagements.")
        else:
            explanation_parts.append("the company is at low social risk, showing strong social practices and positive community and labor relations.")

        explanation_parts.append(f"Finally, the governance risk score is {governance_risk_rating}, which means")
        if governance_risk_rating > 30:
            explanation_parts.append("there are significant governance risks, suggesting serious concerns with board practices, executive compensation, and shareholder rights.")
        elif governance_risk_rating > 20:
            explanation_parts.append("the company has moderate governance risks, indicating room for improvement in governance structures and practices.")
        else:
            explanation_parts.append("the company exhibits low governance risk, reflecting strong governance practices and ethical management.")

        explanation_parts.append("These nuances should be considered when making a final decision, especially when considering individual preferences and concerns.")


    # Combine all parts of the explanation into a single string
    explanation_parts.append(f"\n\tAll nuances, factors, and variables considered, the final decision is: {recommendation}.")
    explanation = " ".join(explanation_parts)

    return recommendation, explanation

# ticker = "F" 
# client_type = "growth"  
# recommendation, explanation = invest(ticker, client_type)
# #recommendation, explanation = invest(ticker)
# print(f"Recommendation: {recommendation}\nExplanation: {explanation}")