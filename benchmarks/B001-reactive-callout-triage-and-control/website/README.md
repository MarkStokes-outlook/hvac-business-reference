# Frostline Mechanical Services — B001 Website

## Overview

This is the generated public website for Frostline Mechanical Services Ltd, produced for benchmark B001 (Reactive Callout Triage and Control).

## Controlling sources

- **Business facts:** `docs/` directory (company profile, services overview, planned and reactive service, installation project delivery, organisation overview, company history, culture and values, customer acquisition, training and competence, service contracts, environmental performance, safety and compliance)
- **Public-brand brief:** `benchmarks/B001-reactive-callout-triage-and-control/public-brand/brand-and-marketing-brief.md`
- **Generation prompt:** `prompts/website-generation.md`

## Implementation

- **Technology:** Static HTML/CSS, no build tools or framework dependencies
- **Pages:** Home, About, Services, Sectors, Careers, Contact, Privacy
- **Visual assets:** SVG illustrations (engineering-themed compositions) — photography was not available in the generation environment
- **Responsive:** Designed for desktop and mobile using CSS media queries
- **Navigation:** Conventional header with mobile hamburger toggle

## Design decisions

- **Colour palette:** Dark blue (#1a3a5c), teal accent (#3a8fb7), warm orange CTA (#e87c3e), neutral greys — cool-toned, professional, consistent with HVAC/engineering positioning
- **Typography:** System sans-serif stack (Inter preferred where available)
- **Layout:** Conventional brochure-site patterns — hero, service cards, two-column features, CTA banners, standard footer
- **Imagery:** SVG compositions depicting rooftop plant, maintenance operations, reactive response workflow, installation projects, team/depot, sector buildings and career progression — reused across pages for consistency
- **Brand device:** Simple circular logo mark with temperature/airflow motif

## Configurable placeholders

The following items are marked as configurable placeholders throughout the site:

- `[Telephone]` — public telephone number
- `[Email]` — public email address
- `[Address]` / `[Office address]` — office or correspondence address
- `[Company registration details]` / `[Registered address]` — for privacy page
- Form action (`action="#"`) — form submission endpoint

These appear in square brackets and italic styling where visible to visitors. They are intentionally not populated with fictional data.

## Validation performed

- All pages checked for consistent navigation and internal link integrity
- Responsive layout verified at typical desktop (1200px+) and mobile (375px) widths via CSS inspection
- SVG assets reference-checked for correct paths from both root and `/pages/` subdirectory
- No unsupported factual claims, named customers, invented certifications or fabricated statistics
- No internal governance, benchmark or operational material exposed in public pages
- No lorem ipsum, TODO markers or image-description placeholders
- Provenance note present in every page footer

## Limitations

- **Imagery:** The generation environment cannot produce photography. All visual assets are SVG illustrations and branded compositions. A production deployment would benefit from commissioned or licensed commercial photography as described in the brand brief.
- **Form functionality:** The contact form has no backend. The `action="#"` attribute would need replacing with a real endpoint.
- **Font loading:** The CSS references Inter via system font stack. No hosted web font is included — adding a Google Fonts or self-hosted Inter would improve typographic consistency.

## File structure

```
website/
├── index.html
├── css/
│   └── style.css
├── assets/
│   ├── logo.svg
│   ├── hero-graphic.svg
│   ├── service-maintenance.svg
│   ├── service-reactive.svg
│   ├── service-installation.svg
│   ├── about-team.svg
│   ├── sectors-graphic.svg
│   └── careers-graphic.svg
├── pages/
│   ├── about.html
│   ├── services.html
│   ├── sectors.html
│   ├── careers.html
│   ├── contact.html
│   └── privacy.html
└── README.md
```
