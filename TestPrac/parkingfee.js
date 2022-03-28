const fees = [120, 0, 60, 591];
const records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"];


function solution(fees, records) {
    const [avgTime, minFee, perTime, perFee] = fees;

    function convertTime(time) {
        let newTime = time.split(':');
        const [hour, minute] = newTime;
        let numHour = parseInt(hour)
        let numMinuite = parseInt(minute)
        return (numHour * 60) + numMinuite;
    }
    function calculFee(usingTime) {
        let totalFee = 0;
        if (usingTime <= avgTime) {
            totalFee = minFee;
        } else {
            let overTime = usingTime - avgTime;
            totalFee = minFee + (Math.ceil(overTime / perTime) * perFee);
        }

        return totalFee;
    }

    function parsingCars(inAndOuts) {
        const carRecord = {};
        inAndOuts.map((record) => {
            const [inTime, carId, isIn] = record.split(' ');
            carRecord[carId] = []
        })
        inAndOuts.map((record) => {
            const [inTime, carId, isIn] = record.split(' ');
            carRecord[carId].push(inTime);
        })
        for (const key in carRecord) {
            if (carRecord[key].length % 2 != 0) {
                carRecord[key].push('23:59');
            }
        }
        return carRecord;
    }
    
    function getUsingTime(carRecord) {
        const carFee = {};
        for (const key in carRecord) {
            let totalUsing = 0;
            for (let i = 0; i < carRecord[key].length; i+=2) {
                totalUsing += convertTime(carRecord[key][i+1]) - convertTime(carRecord[key][i]);
            }
            carFee[key] = totalUsing;
        }
        let sortobj = [];
        for (let number in carFee) {
            sortobj.push([number, carFee[number]]);
        }
        sortobj.sort(function(a, b) {
            return a[0] - b[0];
        });
        return sortobj;
    }
    const carMap = parsingCars(records);
    const sortUsingTime = getUsingTime(carMap);
    var answer = [];
    sortUsingTime.map((user) => {
        answer.push(calculFee(user[1]))
    })

    return answer;
}

solution(fees, records);
