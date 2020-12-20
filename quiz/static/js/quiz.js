
function submitAnswers(answers){

	var total = answers.length;
	var score = 0;
	var choice = []

	for(var i = 1; i <= total; i++){
		
		choice[i] = document.forms["quizForm"]["q"+i].value;
	}
 
	for(i = 1; i <= total; i++){
		if(choice[i] == null || choice[i] == ''){
			alert('You missed question ' + i);
			return false;
		}
	}

	for(i = 1; i <= total; i++){
		if(choice[i] == answers[i - 1]){
			score++;
		}
	}

	var results = document.getElementById('results');
	results.innerHTML = "<h2><b>Congratulations, You have scored" + score + " out of " + total + "</b></h2>"
	return false;
}

