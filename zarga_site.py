<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FitPlan Pro - برنامج التمارين الأسبوعي</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
            color: #333;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        header {
            background: linear-gradient(135deg, #6e48aa, #9d50bb);
            color: white;
            padding: 20px 0;
            text-align: center;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        h1 {
            margin: 0;
            font-size: 2.5em;
        }
        .days {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            justify-content: center;
            margin-bottom: 30px;
        }
        .day {
            background: white;
            border-radius: 10px;
            padding: 15px 25px;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            font-weight: bold;
        }
        .day:hover {
            transform: translateY(-5px);
            background: #6e48aa;
            color: white;
        }
        .workout-details {
            background: white;
            border-radius: 10px;
            padding: 25px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            display: none;
        }
        .workout-details h2 {
            color: #6e48aa;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
        }
        .exercise {
            margin: 15px 0;
            padding: 10px;
            background: #f9f9f9;
            border-radius: 5px;
        }
        .rest-day {
            text-align: center;
            font-size: 1.5em;
            color: #9d50bb;
            padding: 50px 0;
        }
        @media (max-width: 768px) {
            .days {
                flex-direction: column;
                align-items: center;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>FitPlan Pro</h1>
            <p>برنامج التمارين الأسبوعي الأفضل لتحقيق أهدافك</p>
        </header>

        <div class="days">
            <div class="day" onclick="showWorkout('monday')">الاثنين</div>
            <div class="day" onclick="showWorkout('tuesday')">الثلاثاء</div>
            <div class="day" onclick="showWorkout('wednesday')">الأربعاء</div>
            <div class="day" onclick="showWorkout('thursday')">الخميس</div>
            <div class="day" onclick="showWorkout('friday')">الجمعة</div>
            <div class="day" onclick="showWorkout('saturday')">السبت</div>
            <div class="day" onclick="showWorkout('sunday')">الأحد</div>
        </div>

        <div id="workout-display" class="workout-details">
            <!-- سيتم عرض التمارين هنا -->
        </div>
    </div>

    <script>
        const workouts = {
            monday: [
                "Shoulder Press 33×3",
                "Push Up 30×3",
                "Punch Sand Bag 4:00",
                "Floor Press 28×4",
                "Diamond Push Up 15×3",
                "Punishing Bag 3:00",
                "Pull Up 20×3",
                "Jumping Rope 3:00×5"
            ],
            tuesday: [
                "Shoulder Press 33×3",
                "Push Up 30×3",
                "Punch Sand Bag 4:00",
                "Floor Press 28×4",
                "Diamond Push Up 15×3",
                "Punishing Bag 3:00",
                "Pull Up 20×3",
                "Jumping Rope 3:00×5"
            ],
            wednesday: [
                "Crunch 30×4",
                "Leg Raises 20×3",
                "Squat 40×3",
                "Calf Raises 35×3",
                "Squat and Jump 20×3",
                "Jumping Rope 3:00×3"
            ],
            thursday: ["راحة"],
            friday: [
                "Biceps Curl 17×4",
                "Reverse Curl 15×5",
                "Chin Up 22×3",
                "Deadlift 30×5",
                "Squat 30×6",
                "Bridges 45×3",
                "Jumping Rope 3:00×5",
                "Push Up 30×3",
                "Knee Raises 4:00×3"
            ],
            saturday: [
                "Floor Press 22×4",
                "Push Up 25×4",
                "Pull Up 20×3",
                "Biceps Curl 17×3",
                "Shoulder Press 22×4",
                "Chin Up 20×4",
                "Reverse Curl 15×5",
                "Jumping Rope 3:00×3",
                "Squat 30×3",
                "Bridges 30×3"
            ],
            sunday: ["راحة"]
        };

        function showWorkout(day) {
            const display = document.getElementById('workout-display');
            const workout = workouts[day];
            
            let html = `<h2>${getDayName(day)}</h2>`;
            
            if (workout[0] === "راحة") {
                html += `<div class="rest-day">يوم راحة - استمتع بوقتك!</div>`;
            } else {
                workout.forEach(ex => {
                    html += `<div class="exercise">${ex}</div>`;
                });
            }
            
            display.innerHTML = html;
            display.style.display = 'block';
        }

        function getDayName(day) {
            const names = {
                monday: "الاثنين",
                tuesday: "الثلاثاء",
                wednesday: "الأربعاء",
                thursday: "الخميس",
                friday: "الجمعة",
                saturday: "السبت",
                sunday: "الأحد"
            };
            return names[day];
        }
    </script>
</body>
</html>
