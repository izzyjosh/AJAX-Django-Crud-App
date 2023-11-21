// create person

$("#create-form").on("submit", function (e) {
  e.preventDefault();
  let output = "";
  let display = $(".display");
  let userdata = {
    id: $("input[name='p_id']").val(),
    first_name: $("input[name='first_name']").val(),
    last_name: $("input[name='last_name']").val(),
    department: $("input[name='department']").val(),
    course: $("input[name='course']").val(),
  };
  $.ajax({
    url: "{% url 'create' %}",
    method: "POST",
    data: userdata,
    success: function (data) {
      let p = data.person_data;
      if (data.status == "saved") {
        for (i = 0; i < p.length; i++) {
          output += `
      <tr id="${p[i].id}">
          <td>${p[i].id}</td>
          <td>${p[i].first_name}</td>
          <td>${p[i].last_name}</td>
          <td>${p[i].department}</td>
          <td>${p[i].course}</td>
          <td>
          <input type="button" class="btn btn-sm btn-warning mb-1" value="edit" data-sid="${p[i].id} id="edit-btn"">
          <input type="button" class="btn btn-sm btn-danger mb-1" value="delete" data-sid="${p[i].id} id="delete-btn">
          </td>
      </tr>`;
        }
        $("#tbody").html(output);
      }
      e.target.reset();
    },
  });
});

// Delete person
$("#tbody").on("click", "#delete-btn", function () {
  const id = $(this).attr("data-sid");
  const mydata = { id: id };
  $.ajax({
    url: "{% url 'delete' %}",
    method: "POST",
    data: mydata,
    success: function (data) {
      if (data.status === 1) {
        $("#" + id).remove();
      }
    },
  });
});

//update person

$("#tbody").on("click", "#edit-btn", function () {
  const id = $(this).attr("data-sid");
  const mydata = { id: id };
  $.ajax({
    url: "{% url 'update' %}",
    method: "POST",
    data: mydata,
    success: function (data) {
      $("input[name='p_id']").val(`${data.id}`);
      $("input[name='first_name']").val(`${data.first_name}`);
      $("input[name='last_name']").val(`${data.last_name}`);
      $("input[name='department']").val(`${data.department}`);
      $("input[name='course']").val(`${data.course}`);
    },
  });
});
