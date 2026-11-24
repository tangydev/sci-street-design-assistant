# Street Design Assistant: result viewer

Prototype of Design 1 (Task 3.1/3.2, Part B). A single static page that reads a design record (JSON) and shows the outcome, options, cross-section, width chart and checks. It computes nothing new: every number on screen comes from the record (converted from metres to feet for display).

## Run it locally

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

Opening `index.html` by double-click won't work: browsers block a page from reading local files.

## Publish on GitHub Pages

Repository → Settings → Pages → Source: "Deploy from a branch", branch `main`, folder `/ (root)`. The page appears at `https://<user>.github.io/sci-street-design-assistant/`.

## Demo records

| File | Outcome |
| --- | --- |
| `records/example1.json` | Feasible |
| `records/example2.json` | Infeasible |
| `records/example3.json` | Unresolved |

The dropdown also has a "Broken file" entry that points to a missing file, to show the error state.

## Fields added to the record format

These are not in the brief's example format. The viewer shows "no data" when they're missing.

- `street`, `block`: where the task is
- `constraints`: the constraints the engineer confirmed in step 1
- `existing_elements`: today's cross-section, for the before/after comparison

## Not yet done (Task 3.2)

- FastAPI backend serving the records (this prototype reads them as static files)
- The three automated tests
- Timed test with a new user
