HOW IT WORKS
==============================
This program analyzes various aspects of the given stock. It begins by considering more broad aspects of the stock that would apply for any portfolio in order to provide context on how the stock is performing. 

The "broad" data it checks is:
- market sentiment (bear or bull?)
- the market cap of the stock
- the volatility of the stock
- how does it perform compared to stocks in its sector

After considering the broad data, if the ticker was none of the three options (income, growth, esg), then it gives a reccomendation based a following counter of either hold, buy, or sell, and how it matches up in the end.

However, in the case where we have either income, growth, or ESG, things start getting slightly more complicated.

INCOME
===================
We consider dividend yields compared to the dividend yields of the sp500 - if we have that, then buy. If it's a big stock and its not very volatile, then hold because this is a good long term steady option. Otherwise, sell.

Then, consider the five year dividends. If they're good, add that context. If they're not good, then add context, but if we're holding and it's not good, then change to sell as this means the dividend yields have been good recently, but that the long term data says otherwise. 

Then consider payout ratio, in which most cases only adds context, but in the case where the company isn't investing a lot into itself then sell, as this means that it is too risky of an investment. 
===================

GROWTH
===================
For the growth case, we will look at what type of market we're in. If we're in a bull market, the beta is greater than 1, and the strong growth rate, then we shoudl definitely buy, as we have a lot of potential for growth. Also, if were in a bear market and have a positive growth rate then definitely worth it to consider buying. Otherwise, this is likely a strong sell. 

Consider payout ratio next, which in this context of growth is a huge indicator. If we have a very low reinvestment, we most likely want to sell, and in the other cases we consider this too. 

Finally, we calculate our final decision based on the final values of buy sell and hold, following the values from the broad analysis and from the narrow growth analysis. 
===================

ESG
===================
ESG is rather simple, as it makes the decision solely off of whether the risk rating is in the lower end of risk, or if its in the higher end of risk. While this decision is made more simply, considering the context of a ESG-oriented portfolio, the explanation is much more complex, as it considers each individual variable of the ESG score in order for the user to be able to make a more focused decision that prioritizes their individual worries and concerns. 
===================

TRANSCRIPT
================================
AAPL - income

Recommendation: buy
Explanation: We are potentially in a bull market, which can be a good time to buy as markets are expected to rise further. The stock is large cap, meaning it is considered more stable and could provide steady but low returns. The stock is more volatile than the average of the S&P 500, indicating higher risk, but also higher potential reward. The stock's growth is underperforming compared to other stocks in its sector, which indicates potential difficulty growing.
This stock has a strong recent dividend yield when compared to the SP500, making it suitable for income-focused portfolios. 
Know that the five year average of dividend yields is strong. This makes it suitable in a more long-term steady approach. Also, the company is retaining and reinvesting a large portion of income into growth, so this could be a safer stock, but not one focused on income. 
All nuances, factors, and variables considered, the final decision is: buy.

AAPL - esg

Recommendation: buy
Explanation: We are potentially in a bull market, which can be a good time to buy as markets are expected to rise further. The stock is large cap, meaning it is considered more stable and could provide steady but low returns. The stock is more volatile than the average of the S&P 500, indicating higher risk, but also higher potential reward. The stock's growth is underperforming compared to other stocks in its sector, which indicates potential difficulty growing.
Based on the average threshold for what is a safe ESG risk score, the low ESG risk score aligns with sustainable and socially responsible investing criteria. This ESG risk score stacks well against the risk rating of competitors in the same market, which makes it even more attractive. 
There are specific nuances to consider for each category of ESG, though. First, the environmental risk score is 0.46, which means the company is at low environmental risk, reflecting good environmental practices and minimal sustainability concerns. Second, the social risk score is 7.39, which means the company is at low social risk, showing strong social practices and positive community and labor relations. Finally, the governance risk score is 9.37, which means the company exhibits low governance risk, reflecting strong governance practices and ethical management. These nuances should be considered when making a final decision, especially when considering individual preferences and concerns. 
All nuances, factors, and variables considered, the final decision is: buy.

NVDA - growth

Recommendation: buy
Explanation: We are potentially in a bull market, which can be a good time to buy as markets are expected to rise further. The stock is large cap, meaning it is considered more stable and could provide steady but low returns. The stock is more volatile than the average of the S&P 500, indicating higher risk, but also higher potential reward. This stock's growth is outperforming other stocks in its same sector, which indicates competitive advantage and potential for growth.
Given the bull market, high beta and strong growth rate, we can expect significant growth potential. Also, the company is retaining and reinvesting a large portion of income into growth, so this stock could exhibit a lot of growth in the coming years. Given the overall analysis, this stock shows strong potential for growth, aligning with a growth-focused investment strategy. 
All nuances, factors, and variables considered, the final decision is: buy.

AMZN - income

Explanation: We are potentially in a bull market, which can be a good time to buy as markets are expected to rise further. The stock is large cap, meaning it is considered more stable and could provide steady but low returns. The stock is more volatile than the average of the S&P 500, indicating higher risk, but also higher potential reward. This stock's growth is outperforming other stocks in its same sector, which indicates competitive advantage and potential for growth.
Lack of significant dividend yield or steady growth makes this stock less suitable for income-focused portfolios. 
Know that the five year average of dividend yields is strong. This makes it suitable in a more long-term steady approach. Also, the company is retaining and reinvesting a large portion of income into growth, so this could be a safer stock, but not one focused on income. 
All nuances, factors, and variables considered, the final decision is: sell.

GOLD - esg

Recommendation: sell
Explanation: We are potentially in a bull market, which can be a good time to buy as markets are expected to rise further. The stock is large cap, meaning it is considered more stable and could provide steady but low returns. The stock is more volatile than the average of the S&P 500, indicating higher risk, but also higher potential reward. The stock's growth is underperforming compared to other stocks in its sector, which indicates potential difficulty growing.
Based on the average threshold for what is a safe ESG risk score, the high ESG risk score suggests the company does not meet preferred ESG criteria. This ESG risk score stacks well against the risk rating of competitors in the same market, which makes it even more attractive. 
There are specific nuances to consider for each category of ESG, though. First, the environmental risk score is 15.94, which means the company is at low environmental risk, reflecting good environmental practices and minimal sustainability concerns. Second, the social risk score is 11.95, which means the company is at low social risk, showing strong social practices and positive community and labor relations. Finally, the governance risk score is 5.46, which means the company exhibits low governance risk, reflecting strong governance practices and ethical management. These nuances should be considered when making a final decision, especially when considering individual preferences and concerns. 
All nuances, factors, and variables considered, the final decision is: sell.

ALB - growth 

Recommendation: sell
Explanation: We are potentially in a bull market, which can be a good time to buy as markets are expected to rise further. The stock is large cap, meaning it is considered more stable and could provide steady but low returns. The stock is more volatile than the average of the S&P 500, indicating higher risk, but also higher potential reward. The stock's growth is underperforming compared to other stocks in its sector, which indicates potential difficulty growing.
Limited growth potential indicated by market conditions and stock's beta or growth rate. Also, the company is retaining and reinvesting a large portion of income into growth, so this stock could exhibit a lot of growth in the coming years. Considering the analysis, the stock may not meet the growth expectations or presents higher risks compared to potential rewards. 
All nuances, factors, and variables considered, the final decision is: sell.

ALB - income

Recommendation: buy
Explanation: We are potentially in a bull market, which can be a good time to buy as markets are expected to rise further. The stock is large cap, meaning it is considered more stable and could provide steady but low returns. The stock is more volatile than the average of the S&P 500, indicating higher risk, but also higher potential reward. The stock's growth is underperforming compared to other stocks in its sector, which indicates potential difficulty growing.
This stock has a strong recent dividend yield when compared to the SP500, making it suitable for income-focused portfolios. 
Know that the five year average of dividend yields is strong. This makes it suitable in a more long-term steady approach. Also, the company is retaining and reinvesting a large portion of income into growth, so this could be a safer stock, but not one focused on income. 
All nuances, factors, and variables considered, the final decision is: buy.

HYZN - no specification

Recommendation: sell
Explanation: We are potentially in a bull market, which can be a good time to buy as markets are expected to rise further. The stock has a lower market cap, suggesting higher potential for growth and returns, but with higher investment risk. The stock is more volatile than the average of the S&P 500, indicating higher risk, but also higher potential reward. The stock's growth is underperforming compared to other stocks in its sector, which indicates potential difficulty growing.

F - no specification

Recommendation: sell
Explanation: We are potentially in a bull market, which can be a good time to buy as markets are expected to rise further. The stock is large cap, meaning it is considered more stable and could provide steady but low returns. The stock is more volatile than the average of the S&P 500, indicating higher risk, but also higher potential reward. The stock's growth is underperforming compared to other stocks in its sector, which indicates potential difficulty growing.

F - growth

Recommendation: hold
Explanation: We are potentially in a bull market, which can be a good time to buy as markets are expected to rise further. The stock is large cap, meaning it is considered more stable and could provide steady but low returns. The stock is more volatile than the average of the S&P 500, indicating higher risk, but also higher potential reward. The stock's growth is underperforming compared to other stocks in its sector, which indicates potential difficulty growing.
Limited growth potential indicated by market conditions and stock's beta or growth rate. Also, the company has a balanced approach to growth and paying dividends, so this could be a safe approach if also considering income. There are mixed signals regarding the stock's growth potential, suggesting a cautious approach until clearer trends emerge. 
All nuances, factors, and variables considered, the final decision is: hold.

