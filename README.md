# Street Design Assistant: result viewer

Prototypes for Task 3.1/3.2, Part B. One static page reads a design record (JSON) and shows it in three designs, which you switch between with the buttons at the top:

1. **Interactive**: everything on one screen. Pick an option, compare it with today, read its checks.
2. **Report**: one page read top to bottom. The answer first, then why, then the details. It can be printed or saved as a PDF.
3. **Street first**: a top-down road view with flags at each station. Click a flag to see what was checked there.

The page computes nothing new: every number on screen comes from the record (converted from metres to feet for display). The design record menu applies to all three designs. You can link to one design with `#design-1`, `#design-2` or `#design-3`.

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
