clear 

rm -rf JudgeResponse.txt;

echo "JUDGE RESPONSE "> JudgeResponse.txt;
max=3;

for i in `seq 1 $max`
do
  echo "Subtask#$i ";
    echo "Subtask#$i ">> JudgeResponse.txt;
    rm -rf result.txt;
    echo ""> result.txt
    bash LONGSEQ.sh > result.txt| cat result.txt;
    cat result.txt;
done
    cat JudgeResponse.txt;
