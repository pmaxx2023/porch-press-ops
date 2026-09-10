# PP-BING-ADS-001 — $15 Microsoft Search purchase-intent test

**Version:** 3.0 · 2026-09-10  
**Status:** Ready to build paused; not known to be launched; $0 of this authorization recorded as spent  
**Authority:** Maximum **$15 USD total Microsoft media spend**. No transfer, extension, or additional spend.  
**Offer:** *Baby in a Basket* at **$19.99**  
**Destination:** `https://porchpress.store/pages/genealogy-mystery-case`  
**Public truth:** fictional genealogy mystery · printable digital PDFs · nothing ships

## Decision

Determine whether people already searching for a printable genealogy or family-history mystery show enough purchase intent to buy *Baby in a Basket* at $19.99 through a message-matched landing page.

This is one exploratory path, not an A/B test or profitability validation. One purchase is a directional positive signal; it does not prove repeatable acquisition.

## Measurement

- Primary: completed full-price purchases attributed to eligible Microsoft campaign sessions.
- Secondary: search impressions, clicks, CPC, qualified landing sessions, add-to-cart, and checkout start.
- Attribution key: `utm_campaign=pp_bing_ads_001`.
- Do not count homepage visits, free-case sessions, other sources, or bot/test activity as campaign conversions.

## Budget protection

Microsoft daily budgets may overdeliver. Use the first account-supported option that genuinely keeps this test within $15 total:

### Option A — isolated $15 account limit

Use only if the account exposes either a $15 insertion-order/account cap or an isolated prepaid balance of no more than $15 with auto-recharge off and no other campaign able to consume it. Set this campaign to $5/day and a platform end date no later than three calendar days after activation. The account limit, not the daily setting, is the controlling ceiling.

### Option B — platform monthly maximum

If no isolated account limit exists, verify in the live account that a new unshared `DailyBudgetStandard` Search campaign is governed by Microsoft's monthly maximum of daily budget × days in the month. If verified, use `$0.50/day` and an ad-group end date of `2026-09-30`, 11:59 p.m. in the account time zone. For September's 30 days, the platform maximum is $15.

If neither protection is available or verifiable, keep the campaign paused and report `BLOCKED — NO HARD CAP`. Do not substitute `$5/day × 3`, rely on a manual calendar reminder, or assume a scheduled end alone prevents overdelivery.

## Campaign settings

| Setting | Required value |
| --- | --- |
| Campaign | `PP-BING-ADS-001` |
| Type | Expert mode · Search only |
| Ad group | `AG1_GENEALOGY_INTENT` |
| Final URL | `https://porchpress.store/pages/genealogy-mystery-case` |
| Geo | United States |
| Location intent | People physically in the targeted location |
| Language | English |
| Search network | Microsoft owned-and-operated only |
| Syndicated partners | Off |
| Audience Network | Excluded / `-100%` where applicable |
| AI Search | Off where exposed |
| Final URL expansion | Off |
| Search Term Matching | Off |
| Auto-generated text/images | Off |
| Auto-apply recommendations | Off |
| Devices | All |
| Bid strategy | Maximize Clicks with $1.00 maximum CPC |
| Ads | One responsive search ad |

## Keywords

Exact:

- `[printable genealogy mystery]`
- `[genealogy mystery game]`
- `[printable genealogy game]`
- `[family history mystery game]`
- `[genealogy puzzle printable]`
- `[genealogy case file game]`

Phrase:

- `"printable genealogy mystery"`
- `"genealogy mystery game"`
- `"printable genealogy game"`
- `"family history mystery game"`
- `"genealogy puzzle printable"`
- `"genealogy case file game"`

No broad match. If delivery is zero, inspect keyword status and volume before changing anything.

## Negative phrase terms

`free`; `template`; `blank`; `worksheet`; `school`; `lesson plan`; `kids`; `children`; `book`; `novel`; `reddit`; `wikipedia`; `youtube`; `podcast`; `job`; `salary`; `course`; `class`; `dna test`; `23andme`; `ancestry subscription`; `genealogy software`; `family tree maker`; `genealogy research service`; `hire a genealogist`; `murder mystery party`; `party kit`; `escape room near me`; `baby shower`; `gift basket`; `bassinet`.

## Responsive search ad

Pin headline 1 to `The Answer Is in the Records` and headline 2 to `Printable Genealogy Mystery`. Leave the remaining headlines eligible for position 3.

Headlines, each 30 characters or fewer:

1. `The Answer Is in the Records`
2. `Printable Genealogy Mystery`
3. `Open Baby in a Basket`
4. `Who Was She Before Sutton?`
5. `A Complete Case for $19.99`
6. `20 Fictional Record Exhibits`
7. `Progressive Hints Included`
8. `Play Solo or Together`
9. `Download After Purchase`
10. `No Host or Outside Research`
11. `Printable PDF Case Files`
12. `Compare Census Records`

Descriptions, each 90 characters or fewer:

1. `A fictional genealogy case with every clue, progressive hints and a sealed solution.`
2. `Trace Mabel's identity through fictional census and birth records. PDF case—$19.99.`
3. `Compare 20 fictional exhibits and make your case. Play solo or together—no host needed.`
4. `A complete fictional mystery for family-history fans. Printable PDFs; nothing ships.`

Display paths:

- `genealogy`
- `mystery-case`

Final URL suffix, without a leading `?` or `&`:

`utm_source=bing&utm_medium=cpc&utm_campaign=pp_bing_ads_001&utm_content={AdId}&utm_term={Keyword}`

Callouts only; no sitelinks:

- Digital PDF Download
- Printable PDFs
- No Shipping
- Solo or Together
- Hints Included
- Complete Solution

## Verification before activation

- Search landing page is live, $19.99, and contains the working Baby product form.
- Final URL and UTM suffix survive preview.
- Account currency/time zone and actual $15 cap are recorded.
- No other campaign can consume the cap.
- Search partners and Audience Network are excluded.
- Automated expansion/creative is disabled where available.
- Shopify can distinguish this campaign's landing sessions and purchases.
- No cart, checkout, or purchase probe is performed.

## Stop and interpretation

Stop for total spend of $15, any broken destination/tracking/network/price, one attributed purchase, eight qualified landings with no add-to-cart, or the configured end date.

| Result | Interpretation |
| --- | --- |
| At least one attributed purchase | Directional positive; preserve search terms and stop for review |
| Checkout but no purchase | Completion friction plausible; inspect before changing ad |
| Add-to-cart but no checkout | Offer-transition friction plausible |
| Eight qualified landings and zero add-to-cart | Stop; query/page/price package missed the operational threshold |
| Fewer than five clicks by end | Inconclusive, not rejection |
| Impressions but weak CTR | Query/ad mismatch plausible; inspect terms first |

Report actual definitions and compatible totals. Do not call a click leader validated demand.

## Official configuration references

- Budget limits and bid strategies: `https://learn.microsoft.com/en-us/advertising/guides/budget-bid-strategies?view=bingads-13`
- Search ad-group network and end-date fields: `https://learn.microsoft.com/en-us/advertising/campaign-management-service/adgroup?view=bingads-13`
- Responsive search ad specifications: `https://learn.microsoft.com/en-us/advertising/campaign-management-service/responsivesearchad?view=bingads-13`
- Search network values: `https://learn.microsoft.com/en-us/advertising/campaign-management-service/network?view=bingads-13`
- US presence-only location intent: `https://learn.microsoft.com/en-us/advertising/campaign-management-service/locationintentcriterion?view=bingads-13`
- URL tracking: `https://learn.microsoft.com/en-us/advertising/guides/url-tracking-upgraded-urls?view=bingads-13`
- AI Search controls: `https://learn.microsoft.com/en-us/advertising/campaign-management-service/aisearchsetting?view=bingads-13`
