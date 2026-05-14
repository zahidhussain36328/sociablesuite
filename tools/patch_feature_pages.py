"""Patch feature HTML pages: meta + hero + section copy. Image src paths unchanged."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def chips_metrics():
    return [
        ("bi bi-graph-up-arrow", "color:#59D8FF", "Reach & impressions"),
        ("bi bi-heart", "color:#BE46FF", "Engagement"),
        ("bi bi-cursor", "color:#5DFF85", "Clicks & traffic"),
        ("bi bi-people", "color:#59D8FF", "Audience growth"),
        ("bi bi-play-btn", "color:#BE46FF", "Video performance"),
        ("bi bi-pie-chart", "color:#fff", "Content mix"),
        ("bi bi-calendar-range", "color:#59D8FF", "Compare periods"),
        ("bi bi-bell", "color:#FFB020", "Spike alerts"),
        ("bi bi-download", "color:#fff", "Exports"),
    ]


def chips_roles():
    return [
        ("bi bi-shield-check", "color:#59D8FF", "Roles & permissions"),
        ("bi bi-person-check", "color:#BE46FF", "Approvers"),
        ("bi bi-pencil", "color:#5DFF85", "Editors"),
        ("bi bi-eye", "color:#FFB020", "Reviewers"),
        ("bi bi-building", "color:#fff", "Client access"),
        ("bi bi-chat-dots", "color:#59D8FF", "Comments"),
        ("bi bi-link-45deg", "color:#BE46FF", "Shared links"),
        ("bi bi-clock-history", "color:#fff", "Activity log"),
        ("bi bi-envelope", "color:#59D8FF", "Notifications"),
    ]


def chips_sources():
    return [
        ("bi bi-rss", "color:#FF8C42", "RSS & feeds"),
        ("bi bi-bookmark-star", "color:#59D8FF", "Saved ideas"),
        ("bi bi-tags", "color:#BE46FF", "Tags & topics"),
        ("bi bi-folder2", "color:#5DFF85", "Collections"),
        ("bi bi-link-45deg", "color:#fff", "Source links"),
        ("bi bi-search", "color:#59D8FF", "Keyword watch"),
        ("bi bi-image", "color:#BE46FF", "Visual inspo"),
        ("bi bi-journal-text", "color:#fff", "Notes"),
        ("bi bi-lightbulb", "color:#FFB020", "Ideas inbox"),
    ]


def chips_outputs():
    return [
        ("bi bi-chat-square-text", "color:#59D8FF", "Captions"),
        ("bi bi-layout-text-window-reverse", "color:#BE46FF", "Threads"),
        ("bi bi-hash", "color:#5DFF85", "Hashtags"),
        ("bi bi-megaphone", "color:#FFB020", "Hooks & angles"),
        ("bi bi-file-earmark-text", "color:#fff", "Long-form snippets"),
        ("bi bi-translate", "color:#59D8FF", "Tone & rewrite"),
        ("bi bi-image", "color:#BE46FF", "Image prompts"),
        ("bi bi-stars", "color:#fff", "AI variants"),
        ("bi bi-lightning-charge", "color:#5DFF85", "Fast drafts"),
    ]


def chips_listen():
    return [
        ("bi bi-at", "color:#59D8FF", "Brand mentions"),
        ("bi bi-hash", "color:#BE46FF", "Keywords"),
        ("bi bi-geo-alt", "color:#5DFF85", "Locations"),
        ("bi bi-person-lines-fill", "color:#fff", "Competitors"),
        ("bi bi-emoji-smile", "color:#FFB020", "Sentiment"),
        ("bi bi-bell", "color:#59D8FF", "Alerts"),
        ("bi bi-rss", "color:#BE46FF", "Industry terms"),
        ("bi bi-chat-left-text", "color:#fff", "Comments"),
        ("bi bi-graph-up", "color:#5DFF85", "Trend signals"),
    ]


def chips_automate():
    return [
        ("bi bi-diagram-3", "color:#59D8FF", "Rules & paths"),
        ("bi bi-clock", "color:#BE46FF", "Schedules"),
        ("bi bi-arrow-repeat", "color:#5DFF85", "Recycling"),
        ("bi bi-inboxes", "color:#fff", "Routing"),
        ("bi bi-plug", "color:#FFB020", "Integrations"),
        ("bi bi-envelope", "color:#59D8FF", "Email alerts"),
        ("bi bi-slack", "color:#E01E5A", "Team pings"),
        ("bi bi-link-45deg", "color:#BE46FF", "Webhooks"),
        ("bi bi-check2-circle", "color:#5DFF85", "Auto-approve"),
    ]


def chips_inbox():
    return [
        ("fab fa-facebook-f", "color:#1877F2", "Facebook"),
        ("fab fa-instagram", "color:#E4405F", "Instagram"),
        ("fab fa-x-twitter", "", "X (Twitter)"),
        ("fab fa-linkedin-in", "color:#0A66C2", "LinkedIn"),
        ("fab fa-tiktok", "", "TikTok"),
        ("fab fa-youtube", "color:#FF0000", "YouTube"),
        ("fab fa-google", "color:#4285F4", "Google Business"),
        ("fab fa-reddit-alien", "color:#FF4500", "Reddit"),
        ("fab fa-mastodon", "color:#6364FF", "Mastodon"),
    ]


PAGES: dict[str, dict] = {
    "analyze.html": {
        "title": "Analyze — Sociable Suite | Social media analytics & reporting",
        "desc": "See what works across every network. Track engagement, reach, and growth with clear dashboards and exports in Sociable Suite.",
        "kw": "social media analytics, reporting, engagement metrics, Sociable Suite, performance dashboards",
        "badge": "Feature · Analyze",
        "h1_pre": "Turn performance data into ",
        "h1_span": "smarter",
        "h1_post": " next steps",
        "sub": "Compare periods, spot trends, and export the numbers your stakeholders actually read—without jumping between native analytics tabs.",
        "users": "Dashboards • exports • answers in one place",
        "feat_comment": "Analyze feature sections",
        "hero_comment": "Hero Section — Analyze feature",
        "chips": chips_metrics(),
        "sections": [
            ("OVERVIEW", "One view across every connected account", "Bring key metrics into a single workspace so marketing, leadership, and clients stay aligned on what is working."),
            ("METRICS", "Measure what matters", "Slice performance by network, campaign, or content type so every post teaches you something for the next one."),
            ("REPORTS", "Reports that arrive on time", "Schedule recurring summaries, export clean CSVs or PDFs, and spend review meetings on strategy—not spreadsheet cleanup."),
            ("TRENDS", "Compare and benchmark", "Stack this week against last month, launch windows, or a competitor pulse so you see momentum before it shows up in revenue."),
            ("GOALS", "Goals your team can track", "Set targets for reach, engagement, or conversions and watch progress in context—not buried three clicks deep."),
            ("INSIGHTS", "Context beside every chart", "Pair numbers with the posts and audiences behind them so you always know what to double down on next."),
        ],
    },
    "automate.html": {
        "title": "Automate — Sociable Suite | Social media workflow automation",
        "desc": "Put routine publishing, routing, and follow-ups on autopilot with rules, schedules, and smart workflows in Sociable Suite.",
        "kw": "social media automation, workflow rules, scheduling, Sociable Suite, marketing automation",
        "badge": "Feature · Automate",
        "h1_pre": "Put busywork on ",
        "h1_span": "autopilot",
        "h1_post": "",
        "sub": "Define what should happen when content is ready, when a mention spikes, or when a campaign ends—so your team focuses on creative work, not copy-paste.",
        "users": "Rules • triggers • fewer manual steps",
        "feat_comment": "Automate feature sections",
        "hero_comment": "Hero Section — Automate feature",
        "chips": chips_automate(),
        "sections": [
            ("OVERVIEW", "Automation that fits real teams", "Start with simple schedules and grow into multi-step flows that keep publishing consistent when calendars get noisy."),
            ("WORKFLOWS", "Build once, run on repeat", "Chain the steps your team already follows—approvals, tagging, recycling, and alerts—into dependable paths that run in the background."),
            ("ROUTING", "Send work to the right person", "Auto-assign reviews, route DMs to specialists, and keep SLAs visible so nothing sits in limbo between tools."),
            ("RECYCLE", "Keep evergreen content working", "Re-queue winners on a cadence you control, with pauses and caps so feeds stay fresh, not robotic."),
            ("INTEGRATIONS", "Connect your stack", "Trigger actions from email, webhooks, or partner tools so Sociable Suite stays the hub—not another silo."),
            ("RELIABILITY", "Guardrails you can trust", "Dry runs, approvals, and logs mean automation saves time without taking risks with your brand voice."),
        ],
    },
    "collaborate.html": {
        "title": "Collaborate — Sociable Suite | Team workflows for social media",
        "desc": "Review, comment, and approve social content in one shared workspace. Keep brand, legal, and marketing aligned with Sociable Suite.",
        "kw": "team collaboration, approvals, social media workflow, Sociable Suite, marketing operations",
        "badge": "Feature · Collaborate",
        "h1_pre": "Ship content together, ",
        "h1_span": "faster",
        "h1_post": "",
        "sub": "Share drafts, collect feedback in context, and lock in approvals before anything goes live—without endless email threads or missing screenshots.",
        "users": "Comments • approvals • one source of truth",
        "feat_comment": "Collaborate feature sections",
        "hero_comment": "Hero Section — Collaborate feature",
        "chips": chips_roles(),
        "sections": [
            ("OVERVIEW", "A workspace built for marketing teams", "Centralize briefs, assets, and feedback so designers, copywriters, and approvers stay in sync from draft to publish."),
            ("ROLES", "Permissions that match how you work", "Give clients view-only access, let creators draft, and reserve publishing to leads—without sharing passwords to native apps."),
            ("REVIEW", "Feedback where the work lives", "Highlight what to change, @mention teammates, and resolve threads on the asset itself—no more “see attached v7_final.pdf”."),
            ("CALENDAR", "Plan as a group", "See what is queued across brands, spot conflicts early, and shift campaigns together from a calendar everyone trusts."),
            ("HANDOFF", "Clean handoffs between teams", "Move content from ideation to production to approval with clear owners at every step."),
            ("AUDIT", "A trail you can stand behind", "Know who edited copy, swapped media, or hit publish when it is time for compliance or client reporting."),
        ],
    },
    "curate.html": {
        "title": "Curate — Sociable Suite | Discover & organize social content",
        "desc": "Capture ideas, organize sources, and build libraries of on-brand content to share—all inside Sociable Suite.",
        "kw": "content curation, social media library, bookmarks, Sociable Suite, content discovery",
        "badge": "Feature · Curate",
        "h1_pre": "Collect ideas that fit your ",
        "h1_span": "brand",
        "h1_post": "",
        "sub": "Save posts, articles, and inspiration in structured libraries so your next campaign starts from a shelf of proven concepts—not a blank page.",
        "users": "Libraries • tags • ready-to-adapt ideas",
        "feat_comment": "Curate feature sections",
        "hero_comment": "Hero Section — Curate feature",
        "chips": chips_sources(),
        "sections": [
            ("OVERVIEW", "Inspiration without the chaos", "Turn scattered saves into an organized pool your team can search, tag, and reuse when the calendar opens up."),
            ("SOURCES", "Bring the outside world in", "Track feeds, bookmarks, and topics you care about so your team always has fresh inputs when it is time to plan the week."),
            ("LIBRARIES", "Libraries that scale with you", "Group by campaign, client, or vertical so creatives and strategists pull from the same approved set of references."),
            ("ATTRIBUTION", "Credit and context, always", "Keep source links and notes attached so repurposing stays respectful—and clear—when you adapt trending formats."),
            ("TAGGING", "Find the right idea in seconds", "Filter by theme, format, or platform so the best-performing concepts surface when you need a fast win."),
            ("PIPELINE", "From spark to scheduled post", "Move a curated clip into drafts, assign a writer, and keep momentum without re-uploading files."),
        ],
    },
    "generate.html": {
        "title": "Generate — Sociable Suite | AI-assisted social content",
        "desc": "Draft captions, threads, hooks, and prompts faster with AI that understands your brand—built into Sociable Suite.",
        "kw": "AI content generator, social captions, content ideas, Sociable Suite, marketing AI",
        "badge": "Feature · Generate",
        "h1_pre": "Create scroll-stopping copy ",
        "h1_span": "in seconds",
        "h1_post": "",
        "sub": "Start from a brief, a link, or a rough note—then iterate in your brand voice until the post feels ready for the calendar, not the back burner.",
        "users": "Drafts • variants • less writer's block",
        "feat_comment": "Generate feature sections",
        "hero_comment": "Hero Section — Generate feature",
        "chips": chips_outputs(),
        "sections": [
            ("OVERVIEW", "Ideation that keeps your voice", "Guide tone, audience, and guardrails so AI suggestions feel like your team wrote them—just at the speed of now."),
            ("OUTPUTS", "Every format you publish", "Spin up short captions, long threads, hashtag sets, and creative prompts from one flow—then drop winners straight into review."),
            ("REPURPOSE", "One idea, many surfaces", "Turn a blog headline into five social angles, a newsletter blurb, and a carousel outline without rewriting from scratch."),
            ("TONE", "Brand-safe by default", "Lock preferred vocabulary, disclaimers, and CTA styles so every variant stays on-message across regions and products."),
            ("HASHTAGS", "Discovery that still feels human", "Suggest tags and hooks that match the post—not generic clouds that ignore context."),
            ("VISUALS", "Prompts for your creative stack", "Pair copy with image prompts your designers can run with, keeping campaigns cohesive end to end."),
        ],
    },
    "monitor.html": {
        "title": "Monitor — Sociable Suite | Brand & keyword listening",
        "desc": "Track mentions, keywords, and conversations across social networks so you catch opportunities and issues early with Sociable Suite.",
        "kw": "social listening, brand monitoring, keyword tracking, Sociable Suite, reputation management",
        "badge": "Feature · Monitor",
        "h1_pre": "Hear every ",
        "h1_span": "important",
        "h1_post": " conversation",
        "sub": "Stream mentions, competitor moves, and industry chatter into one place—then route what matters to the people who can act on it fastest.",
        "users": "Listening streams • alerts • context",
        "feat_comment": "Monitor feature sections",
        "hero_comment": "Hero Section — Monitor feature",
        "chips": chips_listen(),
        "sections": [
            ("OVERVIEW", "Stay ahead of the narrative", "See spikes, sentiment shifts, and emerging topics while they are still manageable—not after they hit mainstream feeds."),
            ("LISTENING", "Streams tuned to your world", "Blend brand names, campaign hashtags, competitor handles, and product terms so your feed stays focused—not flooded with noise."),
            ("ALERTS", "Wake the right people", "Route high-priority mentions to Slack or email, and quiet the rest so on-call teammates trust every ping."),
            ("COMPETITORS", "Benchmark the conversation", "Compare share of voice, campaign timing, and messaging angles without building a second spreadsheet."),
            ("SENTIMENT", "Read the room quickly", "Spot frustration, praise, or confusion at a glance so support and marketing stay coordinated."),
            ("CRISIS", "Prepared when volume spikes", "When mentions accelerate, keep a single timeline, owners, and response templates ready in one workspace."),
        ],
    },
    "respond.html": {
        "title": "Respond — Sociable Suite | Unified social inbox",
        "desc": "Reply to comments and messages from every major network in one inbox. Assign, tag, and resolve without switching apps—using Sociable Suite.",
        "kw": "social inbox, DM management, community management, Sociable Suite, customer engagement",
        "badge": "Feature · Respond",
        "h1_pre": "Reply from one ",
        "h1_span": "unified",
        "h1_post": " inbox",
        "sub": "See full threads, customer history, and internal notes side by side—so every response feels personal, even when the team is juggling volume.",
        "users": "One queue • every channel • faster replies",
        "feat_comment": "Respond feature sections",
        "hero_comment": "Hero Section — Respond feature",
        "chips": chips_inbox(),
        "sections": [
            ("OVERVIEW", "Community management without the chaos", "Give moderators a shared queue with status, assignee, and context so nothing falls through when three campaigns go live at once."),
            ("CHANNELS", "Every conversation in one queue", "Pull DMs and comments from the networks you manage into a single triage view—prioritize, assign, and clear the backlog with less tab fatigue."),
            ("MACROS", "Answers you can reuse with care", "Save approved snippets for FAQs, shipping updates, or policy replies—then personalize before send."),
            ("ASSIGN", "Ownership that scales", "Route VIPs to account managers, product questions to experts, and spam to archive without losing the thread."),
            ("CONTEXT", "History beside every message", "See past interactions and internal notes so the next teammate picks up exactly where the last reply left off."),
            ("SLA", "Speed you can measure", "Track first-response time and backlog health so leadership sees how community investment pays off."),
        ],
    },
}


def chip_html(chips: list[tuple[str, str, str]]) -> str:
    lines = []
    for cls, style, label in chips:
        st = f' style="{style}"' if style else ""
        lines.append(
            f'                            <div class="ss-platform-chip"><i class="{cls}"{st}></i>{label}</div>'
        )
    return "\n".join(lines)


def build_main(slug: str, data: dict) -> str:
    sid = slug.replace(".html", "")
    s1, s2, s3, s4, s5, s6 = data["sections"]

    def aid(i: int) -> str:
        return f"{sid}-sec{i}-heading"

    chips_block = chip_html(data["chips"])

    return f'''        <!-- {data["hero_comment"]} -->
        <section id="hero" class="hero section ss-hero ss-page-hero">

            <!-- Animated Background -->
            <div class="ss-grid"></div>
            <div class="ss-gradient ss-gradient-1"></div>
            <div class="ss-gradient ss-gradient-2"></div>


            <div class="container position-relative">

                <div class="row align-items-center justify-content-between gy-5 gx-lg-5">

                    <div class="col-lg-6 text-center text-lg-start">

                        <div class="ss-badge">
                            <span></span>
                            {data["badge"]}
                        </div>

                        <h1 class="ss-title">
                            {data["h1_pre"]}<span>{data["h1_span"]}</span>{data["h1_post"]}
                        </h1>

                        <p class="ss-subtitle">
                            {data["sub"]}
                        </p>

                        <div class="ss-hero-form justify-content-center justify-content-lg-start">

                            <input type="email" placeholder="Enter your email address">

                            <button type="button">
                                Get Started Free
                                <i class="bi bi-arrow-right"></i>
                            </button>

                        </div>

                        <div class="ss-users">
                            <span class="dot"></span>
                            {data["users"]}
                        </div>

                    </div>

                    <div class="col-lg-6 col-xl-5" data-aos="fade-left" data-aos-delay="100">
                        <div class="ss-page-hero-visual">
                            <img src="./assets/img/features/publish/publish.webp"
                                alt="Sociable Suite — {sid} feature"
                                width="640" height="480" loading="eager" class="img-fluid">
                        </div>
                    </div>

                </div>

            </div>

        </section>

        <!-- {data["feat_comment"]} -->
        <section class="ss-feature-showcase section" aria-labelledby="{aid(1)}">
            <div class="container">
                <div class="row align-items-center g-4 g-lg-5">
                    <div class="col-lg-6" data-aos="fade-up">
                        <div class="ss-feature-visual">
                            <img src="./assets/img/features/publish/publish.webp"
                                alt="{s1[1]}" width="640" height="480"
                                loading="lazy" class="img-fluid">
                        </div>
                    </div>
                    <div class="col-lg-6 text-center text-lg-start">
                        <div class="ss-feature-block-heading" data-aos="fade-up" data-aos-delay="80">
                            <span class="ss-why-tag">{s1[0]}</span>
                            <h2 id="{aid(1)}">{s1[1]}</h2>
                            <p class="lead-copy mx-auto mx-lg-0">{s1[2]}</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="ss-feature-showcase section" aria-labelledby="{aid(2)}">
            <div class="container">
                <div class="row align-items-center g-4 g-lg-5">
                    <div class="col-lg-6 text-center text-lg-start" data-aos="fade-up">
                        <span class="ss-why-tag">{s2[0]}</span>
                        <h2 id="{aid(2)}">{s2[1]}</h2>
                        <p class="lead-copy mx-auto mx-lg-0">{s2[2]}</p>
                        <div class="ss-platform-grid mx-auto mx-lg-0">
{chips_block}
                        </div>
                    </div>
                    <div class="col-lg-6" data-aos="fade-up" data-aos-delay="100">
                        <div class="ss-feature-visual">
                            <img src="./assets/img/features/publish/schedule.webp"
                                alt="{s2[1]}" width="640" height="480" loading="lazy"
                                class="img-fluid">
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="ss-feature-showcase section" aria-labelledby="{aid(3)}">
            <div class="container">
                <div class="row align-items-center g-4 g-lg-5">
                    <div class="col-lg-6" data-aos="fade-up">
                        <div class="ss-feature-visual">
                            <img src="./assets/img/features/publish/social-calendar.webp"
                                alt="{s3[1]}" width="640" height="480"
                                loading="lazy" class="img-fluid">
                        </div>
                    </div>
                    <div class="col-lg-6 text-center text-lg-start" data-aos="fade-up" data-aos-delay="80">
                        <span class="ss-why-tag">{s3[0]}</span>
                        <h2 id="{aid(3)}">{s3[1]}</h2>
                        <p class="lead-copy mx-auto mx-lg-0">{s3[2]}</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="ss-feature-showcase section" aria-labelledby="{aid(4)}">
            <div class="container">
                <div class="row align-items-center g-4 g-lg-5">
                    <div class="col-lg-6 text-center text-lg-start" data-aos="fade-up">
                        <span class="ss-why-tag">{s4[0]}</span>
                        <h2 id="{aid(4)}">{s4[1]}</h2>
                        <p class="lead-copy mx-auto mx-lg-0">{s4[2]}</p>
                    </div>
                    <div class="col-lg-6" data-aos="fade-up" data-aos-delay="100">
                        <div class="ss-feature-visual">
                            <img src="./assets/img/features/publish/recycle-post.webp"
                                alt="{s4[1]}" width="640" height="480"
                                loading="lazy" class="img-fluid">
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="ss-feature-showcase section" aria-labelledby="{aid(5)}">
            <div class="container">
                <div class="row align-items-center g-4 g-lg-5">
                    <div class="col-lg-6" data-aos="fade-up">
                        <div class="ss-feature-visual">
                            <img src="./assets/img/features/publish/bulk-upload.webp"
                                alt="{s5[1]}" width="640" height="480" loading="lazy"
                                class="img-fluid">
                        </div>
                    </div>
                    <div class="col-lg-6 text-center text-lg-start" data-aos="fade-up" data-aos-delay="80">
                        <span class="ss-why-tag">{s5[0]}</span>
                        <h2 id="{aid(5)}">{s5[1]}</h2>
                        <p class="lead-copy mx-auto mx-lg-0">{s5[2]}</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="ss-feature-showcase section" aria-labelledby="{aid(6)}">
            <div class="container">
                <div class="row align-items-center g-4 g-lg-5">
                    <div class="col-lg-6 text-center text-lg-start" data-aos="fade-up">
                        <span class="ss-why-tag">{s6[0]}</span>
                        <h2 id="{aid(6)}">{s6[1]}</h2>
                        <p class="lead-copy mx-auto mx-lg-0">{s6[2]}</p>
                    </div>
                    <div class="col-lg-6" data-aos="fade-up" data-aos-delay="100">
                        <div class="ss-feature-visual">
                            <img src="./assets/img/features/publish/preview-post.webp"
                                alt="{s6[1]}" width="640" height="480"
                                loading="lazy" class="img-fluid">
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''


def patch_file(path: Path, data: dict) -> None:
    text = path.read_text(encoding="utf-8")
    slug = path.name

    head = (
        f'    <title>{data["title"]}</title>\n'
        f'    <meta name="description" content="{data["desc"]}">\n'
        f'    <meta name="keywords" content="{data["kw"]}">'
    )
    text_new, n = re.subn(
        r"    <title>.*?</title>\s*<meta name=\"description\" content=\".*?\">\s*<meta name=\"keywords\" content=\".*?\">",
        head,
        text,
        count=1,
        flags=re.DOTALL,
    )
    if n != 1:
        raise RuntimeError(f"{slug}: head replace count {n}")

    main = build_main(slug, data)
    text_new, n2 = re.subn(
        r"        <!-- Hero Section.*?</section>\s*\n\s*<!-- =+?\s*\n\s*CTA SECTION",
        main.rstrip() + "\n\n        <!-- =========================================\n          CTA SECTION",
        text_new,
        count=1,
        flags=re.DOTALL,
    )
    if n2 != 1:
        raise RuntimeError(f"{slug}: main replace count {n2}")

    path.write_text(text_new, encoding="utf-8")
    print("patched", slug)


def main() -> None:
    for name, cfg in PAGES.items():
        patch_file(ROOT / name, cfg)


if __name__ == "__main__":
    main()
