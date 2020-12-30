window.history.forward();
function noBack(){window.history.forward();}

function formCheck(){
	if(!document.testForm.siblings.value){
		alert("형제자매 수를 작성해주세요.")
		document.testForm.siblings.focus();
		return false;
	}
	if(!document.testForm.family.value){
		alert("가족수를 작성해주세요.")
		document.testForm.family.focus();
		return false;
	}
}
$('div.checkbox-group.required :checkbox:checked').length > 0
$('div.perfer-group.required :checkbox:checked').length > 0