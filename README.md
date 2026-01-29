# Procedural-Programming-Python

This payroll application is a piece software that will assist Users in processing any quantity of Employee data. Users will be able to input multiple files of the CSV format from various Departments and receive processed Output files. This software aims to provide a simple and efficient method for the necessary calculations relating to each Employees Gross and Net pay. 

## Files / Functions:

- payroll_processing_app.py
  - main_function()

- read_input.py
  - read_csv()
  - float_data()

- calculate_pay.py
  - calc_gross()
  - add_bonuses()
  - subtract_tax()

- give_output.py
  - give_individual_outputs()
  - give_all_output()
  - what_output()

## Fix when wrong account is used for commits

If you are signed into one of your alternate GitHub accounts and push multiple commits with the wrong author, the following steps will help fix this issue.

### Tips before starting

 - Avoid GitLens, it can edit ".git/rebase-merge/git-rebase-todo" file which will cause issues
 - Never click "Sync" at any point. It is not necessary and will cause issues
 - If Vim opens at any point: Esc -> :wq
 - Only set commits you care to change to "edit", all others can remain as "pick"
 - `git status` can be used in the terminal to verify what stage of the rebase you are on.
 - Don't close the terminal once you begin the process.
 - `git rebase --abort` if you run into issues with the process and want to start again.

### Step 1: Configure VS Code as Git editor (avoids Vim)

`git config --global core.editor "code --wait"`

### Step 2: Start an interactive rebase for the last N commits

`git rebase -i HEAD~N`

'N' is the amount of commits that you want to fix.
Set any commits you want to change from 'pick' -> 'edit'.
Save and close the file, the process should proceed in the terminal.

### Step 3: Amend the commit author for each paused commit

`git commit --amend --author="Correct Name <correct.email@example.com>"`

Save and close the file.

### Step 4: Continue the rebase

`git rebase --continue`

You will alternate steps 3 and 4 for each commit to fix.

### Step 5: Finish the rebase

Once all commits have been fixed you should see the following message in the terminal:

`Successfully rebased and updated refs/heads/main`

If you don't you made need to do Step 4 once more.

### Step 6: Push rewritten commits to GitHub

`git push --force-with-lease`

You can check the commits section of the chosen GitHub repository to verify the changes are correct.

### Optional

`git log --pretty=fuller -N`

Use this to verify the last 'N' amount of commits in the terminal.