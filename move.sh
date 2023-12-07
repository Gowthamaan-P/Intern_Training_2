clear

rm -rf /c/Users/itsve/Documents/####OG_PROJ/'Aerobiosys Intern'/AeroIntern/aeroproj
mkdir /c/Users/itsve/Documents/####OG_PROJ/'Aerobiosys Intern'/AeroIntern/aeroproj
cp -r aeroproj /c/Users/itsve/Documents/####OG_PROJ/'Aerobiosys Intern'/AeroIntern

cd /c/Users/itsve/Documents/####OG_PROJ/'Aerobiosys Intern'/Intern_Training_2

git status
sleep 3
echo "____________________________________________________________________________"
echo "<<<<<<YOUR_BRANCH>>>>>>"
echo "____________________________________________________________________________"
git branch
sleep 3
echo "____________________________________________________________________________"

git add .
git status
sleep 3
echo "____________________________________________________________________________"

echo "Commit message:"
read commit_message

git commit -m "$commit_message"

git status
sleep 3

git push -u origin Venukanthan-BS

cd /c/Users/itsve/Documents/####OG_PROJ/'Aerobiosys Intern'/AeroIntern

echo "MOVED TO NEXT REPO"
echo "____________________________________________________________________________"
pwd


git status
sleep 3
echo "____________________________________________________________________________"
echo "<<<<<<YOUR_BRANCH>>>>>>"
echo "____________________________________________________________________________"

git branch
sleep 3
echo "____________________________________________________________________________"

git add .
git status
sleep 3
echo "____________________________________________________________________________"

git commit -m "$commit_message"

git status
sleep 3

git push -u origin main

