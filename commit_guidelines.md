# Commit Guidelines

Update the version number in pyproject.toml

## Writing Good Commit Messages

A good commit message helps others (and your future self) understand the context and reasoning behind the changes made. Follow these guidelines when writing your commit messages:

### General Format:

```
<type>(<scope>): <message>
```

- **`<type>`**: The type of change being made. Examples include:
  - `feat`: A new feature
  - `fix`: A bug fix
  - `docs`: Documentation changes
  - `style`: Code style changes (formatting, missing semicolons, etc.)
  - `refactor`: Refactoring existing code
  - `test`: Adding or modifying tests
  - `chore`: General maintenance or non-feature changes
- **`<scope>`**: A short description of the area of code being changed (optional but helpful). Example: `ui`, `backend`, `api`.
- **`<message>`**: A brief description of the changes made in the commit.

### Examples:
- `feat(ui): add new login page`
- `fix(auth): fix bug in user authentication flow`
- `docs: update README with new setup instructions`
- `style: improve formatting of login button`

### Body (optional):
If necessary, provide a more detailed explanation of the changes made. Use the body of the message to explain **why** the changes were made, not just **what** was changed. This is particularly useful for larger commits.

Example:

feat(api): add search functionality

- Implemented a search endpoint in the API that allows users to filter results based on query parameters.
- Refactored the data processing logic to handle larger datasets more efficiently.

---

## Pushing Code With and Without Tags

### Why Use Tags?
We use tags in Git to mark specific points in history as important. In the context of Python package development and deployment to PyPI.org, tags help us denote **release versions** of the software. For instance, a tag like `v1.0.0` indicates the first official release version of the project. Tags are critical because they allow us to specify a stable version of the code that can be uploaded to PyPI for distribution. Without tags, it would be hard to determine which commit corresponds to a release version.

### 1. Pushing Code Without Tags

If you have made a commit and are ready to push the changes to the repository, you can use the following command:

```bash
git push origin main
```

This command will push the latest changes from your local `main` branch to the remote `main` branch.

### 2. Pushing Code With Tags

When you are pushing code with a version tag (e.g., `v1.0.0`), follow these steps:

1. **Create a Git Tag:**
   First, create a tag for your commit (usually based on the versioning scheme). Use the following command:

   ```bash
   git tag -a v0.1.1 -m "Release version 0.1.1"
   ```

   Here, `v0.1.1` is the tag name and `"Release version 0.1.1"` is the message for the tag.

2. **Push Code and Tag:**
   After tagging the commit, you can push the tag and the code to the repository with the following command:

   ```bash
   git push origin main --tags
   ```

   This will push both the code and the tags to the remote repository. The `--tags` flag ensures that the tags are pushed along with your commits.

### 3. Pushing a Specific Tag (optional)

If you only want to push a specific tag, you can use the following command:

```bash
git push origin v0.1.1
```

This will push only the specified tag (`v0.1.1` in this case) to the remote repository.

---

## Summary

- Always write descriptive and clear commit messages.
- For tagging, use semantic versioning (e.g., `v0.1.0`).
- Use `git push origin main` to push without tags and `git push origin main --tags` to push both the code and tags.