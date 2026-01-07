### 📓 Micronotes — Simple Notes API (Docker + CI/CD + EC2)

Micronotes is a lightweight Python/Flask notes service designed to demonstrate:

* Containerization with **Docker**
* Local development using **Docker Compose**
* Automated builds and tests using **GitHub Actions**
* Deployment to **AWS EC2**
* Basic monitoring with a health endpoint

It’s intentionally small — so the real focus is on DevOps workflows rather than application complexity.

---

## 🚀 What This App Does

Micronotes exposes a simple REST API:

| Method | Endpoint      | Description          |
| ------ | ------------- | -------------------- |
| GET    | `/notes`      | List all notes       |
| GET    | `/notes/<id>` | Get single note      |
| POST   | `/notes`      | Create a note        |
| GET    | `/health`     | Service health check |

Example response:

```json
[
  {
    "id": 1,
    "title": "First note",
    "content": "Hello from EC2"
  }
]
```

---

## 🏗️ Project Structure

```
micronotes/
│
├── app/
│   ├── main.py           # Flask backend
│   ├── requirements.txt  # App dependencies
│
├── Dockerfile            # Builds the app image
├── docker-compose.yml    # Runs local environment
│
└── .github/workflows/
    ├── docker-compose-cicd.yml   # CI/CD pipeline
    ├── docker-compose.yml        # Build/Test pipeline
    └── deploy-ec2.yml            # Deploy to AWS
```

---

## 🔧 Running Locally (Docker Compose)

Make sure Docker is installed, then run:

```
docker compose up --build
```

API runs at:

```
http://localhost:5000
```

Test:

```
curl http://localhost:5000/notes
curl http://localhost:5000/health
```

---

## 🐳 Docker Image

Build manually (if needed):

```
docker build -t micronotes .
```

Run:

```
docker run -p 5000:5000 micronotes
```

---

## 🤖 CI: Build & Test Pipeline (GitHub Actions)

The CI pipeline:

1️⃣ Checks out repository
2️⃣ Builds Docker images
3️⃣ Validates compose file
4️⃣ Spins up services
5️⃣ Runs basic smoke tests
6️⃣ Cleans up

Triggered on:

```
push
pull_request
```

---

## 🚢 CD: Deploy to AWS EC2

Deployment uses SSH + Docker commands:

* Build image
* Pull latest
* Restart container on EC2

Your EC2 host runs:

```
docker ps
docker pull
docker run -d -p 5000:5000 micronotes
```

And app is reachable (example):

```
http://44.213.102.238:5000/notes
http://44.213.102.238:5000/health
```

---

## 🔐 Required GitHub Secrets

These must exist in:

```
Settings → Secrets → Actions
```

| Secret               | Purpose                        |
| -------------------- | ------------------------------ |
| `EC2_IP`             | Public IP of EC2 instance      |
| `EC2_USER`           | SSH user (ubuntu / ec2-user)   |
| `EC2_SSH_KEY`        | Private PEM key                |
| `DOCKER_USERNAME`    | Docker Hub username            |
| `DOCKER_PASSWORD`    | Docker Hub token               |
| `MYSQL_*` (optional) | DB if using persistent storage |

Important:
Secret names must exactly match what workflows reference.

---

## ✅ Completed So Far

✔ App works locally
✔ Docker image builds
✔ Docker Compose runs
✔ CI pipeline executes
✔ EC2 running container
✔ Public endpoint accessible
✔ Health endpoint works
✔ Mistake documentation added
✔ Git troubleshooting learned
✔ CI/CD debugging experience gained

---

## ⏳ Still Pending / To Improve

🔲 Database persistence (data survives container restart)
🔲 Automated tests instead of manual API checks
🔲 Versioned releases (tags/versions)
🔲 Rollback strategy
🔲 Monitoring / logs forwarding
🔲 Environment-specific pipelines (dev/stage/prod)

These are great future enhancements for your DevOps resume.

---

# 🧠 Mistakes I Made (and What I Learned)

Real DevOps projects rarely run smoothly — and that’s where the learning happens.

Below are the key issues I faced and what they taught me.

---

### 1️⃣ Secrets Naming Confusion (EC2_IP vs EC2_HOST)

Workflows failed because secret names didn’t match config.

**Lesson**

* Secret names must be **consistent**
* Document them clearly in README
* Avoid renaming mid-project

---

### 2️⃣ Accidentally Created a Git Submodule

This triggered CI errors like:

```
fatal: could not read from remote repository
```

**Lesson**

* Submodules complicate repos
* Always inspect `.gitmodules` when weird Git behavior occurs

---

### 3️⃣ Push Rejected Because Remote Was Ahead

```
! [rejected] main -> main (fetch first)
```

**Fix**

```
git pull --rebase origin main
```

**Lesson**

* Always sync remote before pushing
* Rebase keeps history clean

---

### 4️⃣ Rebase Blocked by Unstaged Changes

```
error: cannot pull with rebase: You have unstaged changes
```

**Lesson**

* Git requires a clean working directory
* Use `stash` when unsure

---

### 5️⃣ CI Failed Because Submodules Weren’t Checked Out

Fix:

```yaml
with:
  submodules: recursive
```

**Lesson**

* CI must mirror local repo structure

---

### 6️⃣ Workflow Overlap Confusion

Multiple deploy workflows created chaos.

**Lesson**

* Keep pipelines simple
* One CI + One CD is enough

---

### 7️⃣ Thought API Was Broken (It Was Just Stateless)

Restarting containers wiped data.

**Lesson**

* In-memory storage resets on restart
* Real apps need persistent DB storage

---

### 8️⃣ Burnout From Debugging Loops

Repeating fixes became frustrating.

**Lesson**

* Pause, summarize, then continue
* Good documentation saves time later

---

## 🎯 Why This Documentation Matters

This repo now tells a complete story:

* You built an app
* Dockerized it
* Automated pipelines
* Deployed to cloud
* Debugged real DevOps problems
* Reflected on learning

That’s exactly what interviewers look for.

---

## 🙌 Credits

Built as part of my DevOps learning journey — focusing on CI/CD, automation, and cloud deployment.

---

### ⭐ Improvements Welcome

If you’d like to contribute enhancements or ideas:

```
fork → commit → pull request
```

PRs are always appreciated.

---

## 💬 Want to walk through next steps?

We can also add:

* Diagrams
* Screenshots
* Deployment scripts
* Interview talking points

Just say the word — we’ll continue from here.