<!-- Post Request -->

function create () {
	alert("hello world");
	let userdata = {
		first_name: $("input[name='first_name']").val(),
		last_name: $("input[name='last_name']").val(),
		department: $("input[name='department']").val(),
		course: $("input[name='course']").val(),
	};
	$.ajax({
		url : "{% url 'create' %}",
		method : "POST",
		data: userdata,
		success: function (data) {
			alert(data.status);
		},
	}
	);
};

