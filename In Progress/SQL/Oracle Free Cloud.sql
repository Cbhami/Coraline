SELECT * FROM RUNDATA WHERE ACTIVITY_TYPE = 'Run';

SELECT * FROM RUNDATA WHERE ACTIVITY_TYPE = 'Run' AND CALORIES_BURNED_KCAL > 350 ORDER BY DATE_SUBMITTED DESC, WORKOUT_DATE Desc;