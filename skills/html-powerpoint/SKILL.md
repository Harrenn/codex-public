---
name: html-powerpoint
description: Create high-quality presentation-style slide decks as self-contained HTML, CSS, and JavaScript. Use only when the user explicitly invokes `html_powerpoint` by literal name or explicitly selects `$html-powerpoint`; never activate for generic requests mentioning presentations, slides, PowerPoint, decks, pitch decks, or similar terms, which must use the platform's normal presentation workflow.
---

# HTML PowerPoint

Create a polished browser-based slide deck whose HTML version is the visual source of truth. Optimize for editorial clarity, modern presentation design, portability, and reliable local playback.

## Preserve opt-in behavior

- Treat this workflow as rare-use and explicitly invoked.
- Do not make it the default presentation workflow or modify ordinary presentation behavior.
- If the user requests a presentation without explicitly invoking this skill, use the normal presentation tools instead.

## Plan before implementation

1. Identify the goal, audience, narrative, tone, slide count, brand constraints, content density, animation preference, offline requirement, and export requirement from the request.
2. Turn the material into a coherent storyline. Give every slide one clear communication objective.
3. Choose the visual treatment that best communicates each objective.
4. Establish a small design system: type scale, colors, spacing, grid, graphic language, and transition style.
5. Implement only after the storyline and slide roles are clear.

When essential information is missing, make reasonable assumptions and state them. Do not place paragraphs into arbitrary boxes or default to dense bullet lists.

## Build the deck

Produce a complete presentation that runs locally in a modern browser.

- Prefer one self-contained `.html` file with embedded CSS and JavaScript.
- Keep required local assets beside the HTML in a clearly named asset directory when embedding is impractical.
- Avoid build systems and dependencies unless they materially improve the requested result.
- Prefer plain HTML/CSS/JavaScript for portability and layout control. Use Reveal.js, Slidev, or another framework only when it clearly improves the deck and still meets offline requirements.
- Use semantic, maintainable markup and reusable CSS classes or components.
- Use supplied user images first. Use CSS and SVG for diagrams, abstract graphics, icons, and decorative systems when practical.
- Do not rely on inaccessible remote assets unless the user permits it. Provide sensible fallbacks for any external asset.

## Presentation behavior

Implement these defaults unless the user overrides them:

- Use a 16:9 widescreen slide canvas.
- Give each slide an explicit boundary and stable identity.
- Support Left Arrow, Right Arrow, and Space navigation.
- Add restrained previous/next controls when useful.
- Provide full-screen presentation mode through the browser Fullscreen API.
- Show slide numbering when appropriate.
- Preserve slide composition responsively through controlled scaling rather than uncontrolled reflow.
- Use smooth, restrained transitions and respect `prefers-reduced-motion`.
- Keep the current slide reflected in the URL hash when useful for sharing or reload recovery.
- Ensure controls remain usable by keyboard and have accessible labels.

## Design standard

Aim for professional editorial, keynote, consulting, product-launch, or modern web-design quality appropriate to the subject.

Prioritize:

- Strong typography and deliberate hierarchy.
- Generous spacing and grid-based composition.
- Clear focal points and high-quality visual balance.
- A consistent visual language across the deck.
- Minimal text with purposeful diagrams, charts, cards, timelines, matrices, and callouts.
- Modern CSS capabilities such as grid, flexbox, gradients, masks, SVG, and controlled layering when they communicate or reinforce the concept.

Avoid:

- Generic "AI PowerPoint" layouts.
- Dense bullet dumps or tiny text.
- Repeating one layout on every slide.
- Cheap template aesthetics and generic stock-presentation styling.
- Random icons or decoration without communicative purpose.
- Excessive gradients, glassmorphism, shadows, animation, or visual clutter.

## Use visual variety coherently

Select from multiple layout archetypes as the narrative requires:

- Hero or title.
- Big statement, quote, or key metric.
- Two-column narrative.
- Comparison or before/after.
- Process, system, or architecture diagram.
- Timeline or roadmap.
- Chart-focused composition.
- Image-led slide.
- Matrix or portfolio view.
- Summary or call to action.

Vary layouts without breaking the shared design system. Each visual element must clarify information, establish hierarchy, or advance the story.

## Create presentation-first data visualization

When charts are required:

- Prefer SVG, CSS, Canvas, or a lightweight library only when necessary.
- Label important values directly where practical.
- Remove unnecessary axes, gridlines, legends, borders, and visual noise.
- Emphasize the takeaway rather than recreating a dashboard.
- Ensure labels and values remain readable at presentation distance.
- Include an accessible textual summary for material chart conclusions.

## Use animation sparingly

Use motion only when it supports storytelling or orientation.

- Prefer subtle fade, translate, scale, or progressive reveal effects.
- Keep timings short and consistent.
- Avoid gimmicky transitions, parallax overload, bouncing, spinning, or continuous decorative motion.
- Make the deck fully understandable with animation disabled.

## Prevent overflow and rendering defects

- Treat each slide as a fixed composition and test every slide for overflow.
- Keep text comfortably readable at common laptop and projector resolutions.
- Avoid content touching slide edges or navigation controls.
- Test long titles, tables, charts, code, and citations at the target aspect ratio.
- Verify the first slide, last slide, navigation, full-screen control, URL/hash behavior, and print output.
- Inspect at desktop and narrower viewport sizes when browser tooling is available.
- Fix clipping, unintended scrollbars, overlap, broken assets, and low-contrast content before delivery.

## Support printing and export

When practical, include print CSS with one slide per page:

- Use `@page` with a landscape 16:9 page size or matching custom dimensions.
- Remove navigation controls and interactive chrome in print.
- Prevent slide page breaks and preserve backgrounds when possible.
- Ensure hidden or unrevealed content needed for the final slide appears in print.

If the user requests PDF, prepare the HTML for clean printing and create the PDF when suitable tooling is available.

If the user explicitly requests `.pptx`:

- Keep the HTML deck as the visual source of truth.
- Prefer recreating approved layouts with native PowerPoint elements when feasible.
- If native recreation is impractical, explain the tradeoff between editable PowerPoint elements and slide-sized rendered images.
- Do not silently replace this HTML-first workflow with the standard PowerPoint workflow.

## Deliver files

Provide:

- The final `.html` file.
- Any required asset directory or files.
- PDF or PPTX only when requested.
- A concise instruction to open the HTML in a modern browser, use the arrow keys to navigate, and enter full screen from the deck control or browser.

Follow explicit user instructions on slide count, brand colors, fonts, references, density, animation, framework, offline behavior, and export. When adapting an existing deck or reference, preserve its requested information architecture or visual language while implementing it as HTML slides.
