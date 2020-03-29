python parse.py
git -C ../lois-en-construction-données checkout master
# git -C ../lois-en-construction-données branch -D loi_orientation_mobilites
git -C ../lois-en-construction-données checkout --orphan loi_orientation_mobilites
python gittt.py > gittt.sh
. gittt.sh