const sentence = "i love coding"
const keyword = "mask"
const skips = [0, 0, 3, 2, 3, 4]

function solution (sentence, keyword, skips) {
    let sentenceArr = sentence.split("");
    let initialSentenceLength = sentenceArr.length;
    let initialSkipsLength = skips.length;
    let keywordArr = keyword.split("");
    let pushCount = 0;
    let keywordCount = -1;
    let skipsCount = 0;
    for (let i = 0; i < initialSkipsLength; i++) {
        keywordCount++;
        if (skipsCount > initialSentenceLength) {
            break;
        }
        if (keywordCount === keywordArr.length) {
            keywordCount = 0;
        }
        let putIndex = skips.shift();
        skipsCount += putIndex;
        putIndex = pushCount + skipsCount;
        console.log(putIndex, "putindex", keywordCount, "keywordcount");
        // putindex 이전 값들 중 keyword와 같은 값이 있는지 확인.
        sentenceArr.splice(putIndex, 0, keywordArr[keywordCount]);
        pushCount++;
    }
    var answer = sentenceArr.join('');
    console.log(answer);
}

solution(sentence, keyword, skips);