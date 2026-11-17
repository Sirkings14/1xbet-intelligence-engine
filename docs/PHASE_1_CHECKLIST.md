# Phase 1 acceptance checklist

- [ ] Backend starts locally and /health returns status=ok.
- [ ] Invalid odds <= 1 are rejected.
- [ ] Timestamps without timezone are rejected.
- [ ] Valid observations can be stored and listed.
- [ ] Android app opens on a physical device.
- [ ] Capture permission is requested only after a user tap.
- [ ] Declining permission leaves capture disabled.
- [ ] No credentials, betting actions, or hidden capture exist.
- [ ] OCR text is not considered verified until reviewed.

Do not progress to continuous capture until the permission flow, app terms, and local legal requirements have been checked.
