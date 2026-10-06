# Initial News source access review

Reviewed 2026-10-06 for R1.1 readiness; no acquisition adapter, registry enablement,
news corpus, publisher contact or AI transmission occurred. Official documentation
and feed-link catalogues were read as one-off research. Sources were not probed
for paywall bypass, authenticated endpoints or alternate access around robots denial.
Statuses describe this application's intended professional internal use, not whether
someone can read an ordinary web page. This is a recorded permissions assessment,
not a claim that legal exceptions or a newsroom agreement have been established.

## Small candidate batch and exact URLs

| Candidate ID | Category / tier / origin | Language | Official catalogue and candidate endpoint | Access verification / disposition |
| --- | --- | --- | --- | --- |
| govuk-news-en | official / primary institution / uk-government | en | [Catalogue](https://www.gov.uk/search/news-and-communications?order=updated-newest); [Atom](https://www.gov.uk/search/news-and-communications.atom) | Exact Atom link extracted from official catalogue. Eligible licensed-field candidate; feed response/sample not collected. |
| un-news-ar | official / primary institution / united-nations | ar | [Catalogue](https://news.un.org/ar/rss-feeds); [Headlines RSS](https://news.un.org/feed/subscribe/ar/news/all/rss.xml) | Official catalogue link verified; feed fetch via research browser returned cache miss. Conditional rights; disabled. |
| un-news-en | official / primary institution / united-nations | en | [Catalogue](https://news.un.org/en/rss-feeds); candidate `https://news.un.org/feed/subscribe/en/news/all/rss.xml` | English catalogue denied by research tool robots. Candidate endpoint is not primary-verified in this review; do not assume matching Arabic URL structure proves it. Disabled. |
| qna-general-ar | wire + official / national state agency / qna | ar | [Catalogue](https://qna.org.qa/ar-qa/rss-feeds/); [General RSS link](https://qna.org.qa/ar-QA/Pages/RSS-Feeds/General) | Exact link extracted from official catalogue; no XML/response-shape or article-body inspection. Permission unresolved; disabled. |
| qna-general-en | wire + official / national state agency / qna | en | [Catalogue](https://qna.org.qa/en/RSS-Feeds); [General RSS link](https://qna.org.qa/en/Pages/RSS-Feeds/General) | Exact link extracted from official catalogue; no XML/response-shape or article-body inspection. Permission unresolved; disabled. |

This is five language/feed candidates across three publisher origins, not five
independent corroborating sources. Tiers describe source role, not measured trust.
QNA's quoting a UN statement does not add an independent account. These institutional
sources are useful for statements/events but give an incomplete editorial view.
A permission-cleared independent newsroom source remains a batch prerequisite.
BBC and Al Jazeera were reviewed below as deferred newsroom options, not silently
added through a third-party feed directory.

## GOV.UK English: eligible with field-level restrictions

Basis: official [reuse guidance](https://www.gov.uk/help/reuse-govuk-content),
[OGL v3](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
and [robots](https://www.gov.uk/robots.txt). Licence text was also read directly
successfully when the research browser could not open it.

- Permitted content: qualifying licensed government text/metadata can be copied,
  adapted and used commercially at no licence charge. Start with feed title,
  canonical link, supplied publication/update times and licensed feed excerpt;
  no assumed full article body, images or attachments.
- Restrictions: source/licence attribution; no implied government endorsement.
  Personal data, unlicensed third-party rights, logos and other licence exclusions
  are not covered by this grant. Review item-specific notices; withhold excluded
  fields/content. Robots observations do not expand the licence.
- Retention: licence is perpetual subject to conditions; no content TTL specified.
  Application retention is separately undecided. A 72-hour discovery window is
  not a legal retention rule. Rights-required removal and privacy limits still apply.
- AI transmission: OGL grants transmission/adaptation for qualifying material, but
  contains no provider-specific AI grant. Future inference that licensed text could
  be processed must exclude unlicensed/personal data and review provider terms.
  This is not AI enablement, training permission for excluded data, or G04 acceptance.
- Unresolved: permitted representative fields/sample, current feed behavior,
  cache headers and operational request limits. Use bounded conditional requests
  only after authorization; robots excludes search/all, not the reviewed catalogue
  path. Recheck before acquisition.

## UN News Arabic / English: conditional, not cleared

Basis: official [Arabic RSS documentation](https://news.un.org/ar/rss-feeds) and
[UN copyright](https://www.un.org/en/about-us/copyright/). Copyright page was
available in the primary-source search index; direct request returned 403. English
catalogue was robots-denied; [terms](https://www.un.org/en/about-us/terms-of-use)
and [robots](https://news.un.org/robots.txt) were not fully accessible in this review.

- Permitted content: RSS reader distribution is documented; news reuse is conditional
  on credit and advising the UN. Satisfaction of those conditions for this internal
  tool has not been established; no local-content ingestion permission marked true.
- Restrictions: general reproduction/transmission/storage otherwise requires
  applicable terms or written permission. No blanket rights to third-party images,
  media or entire article bodies inferred.
- Retention: no specific permitted cache/storage duration verified. Do not invent
  a TTL or retain a corpus while this use remains unresolved.
- AI transmission: not explicitly cleared by inspected news-reuse wording. Keep
  forbidden at dispatch until permission and future provider policy are reviewed.
- Unresolved: how to advise UN; whether automated internal editorial indexing,
  local storage and excerpt display fit the news exception; specific retention,
  robots/access limits, current English endpoint and permitted sample. Existing
  newsroom agreement could change status only after its exact scope is reviewed.

## QNA General Arabic / English: access offered; reuse unresolved

Basis: official Arabic/English catalogues above, [terms of use](https://qna.org.qa/en/pages/terms-of-use)
and [robots](https://qna.org.qa/robots.txt) (not accessible through research browser).

- Permitted content: RSS links are intentionally provided. No explicit professional
  internal indexing/storage/excerpt-reuse licence found; all other rights reserved.
- Restrictions: no unavailable-material access or site overburdening; supplier and
  third-party rights remain separate. A licence granted by contributors to QNA is
  not a licence granted by QNA to this application.
- Retention: no permitted cache duration or storage policy established. Disabled
  source means no content retention pending permission.
- AI transmission: no affirmative grant found; not permitted by current application
  assessment. Lack of an AI clause is not approval.
- Unresolved: no-cost automated feed/index/excerpt permission, retention and AI
  scope, actual response/fields, operational limits and current robots directives.
  Resolve via existing agreement or publisher clarification; no contact sent here.

## Deferred independent-newsroom sources

| Source | Official documentation | Permitted use / restrictions | Retention / AI / unresolved |
| --- | --- | --- | --- |
| BBC English, major international public-service newsroom | [Official feed catalogue](https://support.bbc.co.uk/platform/feeds/NewsFeeds.htm), [World edition catalogue](https://support.bbc.co.uk/platform/feeds/NewsHeadlinesWorldEdition.htm), [official historical terms PDF, 31 March 2022](https://downloads.bbc.co.uk/usingthebbc/bbc_terms_of_use_31March2022english.pdf) | Documented feeds are subject to feed terms. Historical terms require permission for business use/metadata and computer analysis and warn fees may apply. Current terms and a no-cost agreement were not verified. No professional collection cleared. | No approved retention or AI transmission. Historical terms are not current entitlement. Current feed endpoint, robots, current terms and free professional permission all unresolved; no feed collected. Official historical OPML URL: `http://news.bbc.co.uk/rss/newsonline_world_edition/feeds.opml`. |
| Al Jazeera Arabic/English, major international newsroom | [Network terms, section 6](https://terms.aljazeera.net/index.html), [Arabic robots notice](https://www.aljazeera.net/robots.txt) | Personal/noncommercial access does not authorize this professional tool. Written permission required for copying/storage/transmission and automated mining/scraping. Robots notice additionally restricts software/AI development and commercial use. | BLOCKED without appropriate written no-cost permission. No approved retention or AI transmission. Do not fetch article/feed data for development; exact current feed URLs were not primary-verified and are not invented here. |

## Activation checklist for the next authorized task

All candidates remain disabled. Record separate local-copy, display, translation,
AI-transmission and training rights; permitted fields; excluded media/third-party
content; attribution; publisher retention limits (unknown stays unknown); an
application retention policy; permission evidence/date/expiry; origin group; robots
and endpoint verification; and observed request limits. No undocumented limit is
encoded as zero or unlimited. Technical HTTP success is not a permission test.

Before dispatch, review a bounded permitted sample and snapshot the applicable
permission/version. Do not put real source excerpts or article corpora into this
public code repository. Keep runtime material locally ignored. If rights mandate
removal, purge covered content/caches/derivatives and preserve only permitted
provenance/tombstones; immutable history is not permission to retain restricted text.
No AI-provider review is needed to show raw links in R1.1. AI remains disabled.
