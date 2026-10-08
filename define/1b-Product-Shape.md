# Product Shape Framework

The structure and guidance for the `## Product Shape` section of `docs/DEFINE.md`, which `define-product-shape` fills — this worksheet itself stays blank. The shape is how the customer receives and uses the product. It decides which Design, Develop, and Distribute steps apply and how each adapts. The twelve shapes and the questions for picking one are in `productos/shapes/SHAPES.md`.

---

## 1. Primary Shape

*Which one shape delivers the value to the first paying customer — and on which platform?*

> Good: "`agent-skill` — a Claude skill pack, installed from our GitHub and listed on the community skill directories"
> Bad: "An AI platform with an app, a plugin, an API and a community" (that's four shapes and no decision)

**Your answer:**

---

## 2. Secondary Shapes

*Which other surfaces does the MVP genuinely ship? None is a fine answer.*

> Good: "`mcp-server`, so agents can query the same data the web app shows — ships in the MVP because the persona works inside Claude all day"
> Bad: "Mobile app later, maybe a Slack bot, possibly an API" (wishes, not MVP surfaces)

**Your answer:**

---

## 3. Why This Shape

*Why does the customer want it in this shape — where do they already work, and what did you reject?*

> Good: "Our accountants already work in Excel and Claude; a web app would be one more tab they don't open. Rejected `web-app` because it moves the work away from where they do it."
> Bad: "Web apps are the standard" (a default, not a reason)

**Your answer:**

---

## 4. Live Means

*What, concretely, makes this product live? (The shape file gives the default bar — make it specific to yours.)*

> Good: "A stranger installs the plugin from the marketplace and gets a reconciled bank statement on the first try."
> Bad: "It's launched"

**Your answer:**

---

## 5. First Sale Means

*What is the first payment event, and how is the money collected?*

> Good: "A firm pays the $49/month licence through a Stripe payment link and activates the key."
> Bad: "People start paying"

**Your answer:**

---

## 6. Build Implications

*What does this shape require that changes the build — a UI, a backend, auth, payments, hosting, a store review, an eval set?*

> Good: "No UI beyond a settings page. Needs a licence-key check, a usage log for activation tracking, and an eval set because the output quality is the product. Marketplace review takes days — plan for it."
> Bad: "Standard stack"

**Your answer:**

---

## 7. Sequence

*Will the product change shape once something is proven? Name the next shape and the trigger. None is a fine answer.*

> Good: "Start as a `productized-service` delivered with our own prompts; move to `web-app` once 10 clients pay and the process is stable."
> Bad: "We'll see"

**Your answer:**
