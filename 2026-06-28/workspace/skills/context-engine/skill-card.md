## Description: <br>
Loads and manages company context for all C-suite advisor skills. Reads ~/.claude/company-context.md, detects stale context (>90 days), enriches context during conversations, and enforces privacy/anonymization rules before external API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alirezarezvani](https://clawhub.ai/user/alirezarezvani) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Founders, executives, and advisor agents use this skill to load a reusable company profile, detect stale or incomplete context, and personalize C-suite advisory sessions while protecting sensitive company information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores and reuses sensitive company profile details in a local context file. <br>
Mitigation: Keep the context file limited to business details suitable for local storage and review proposed updates before allowing writes. <br>
Risk: Company context could expose revenue, runway, customer, employee, investor, or roadmap details during external searches or API calls. <br>
Mitigation: Apply the bundled anonymization protocol and inspect anonymized payloads before using external tools with company information. <br>
Risk: Stale or incomplete company context can lead to poorly calibrated advisory output. <br>
Mitigation: Use the skill's staleness checks, note missing fields, and refresh or confirm assumptions when the context is older than 90 days or incomplete. <br>


## Reference(s): <br>
- [Anonymization Protocol](references/anonymization-protocol.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with prompts and optional local context-file updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads ~/.claude/company-context.md and asks for confirmation before updating the context file.] <br>

## Skill Version(s): <br>
2.1.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
