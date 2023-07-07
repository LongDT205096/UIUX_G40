var i = 14;
var buttons = document.getElementsByName("deletetask");
document.getElementById("addTaskBtn").addEventListener("click", function(event) {
    event.preventDefault(); // Ngăn chặn hành vi mặc định của nút submit
    // Lấy giá trị từ các trường input
    i++;
    var title = document.getElementById("title_task-a").value;
    
    var priority = document.getElementById("priority").value;
    var status = document.getElementById("status").value;
    var date = document.getElementById("date-picker").value;
    var type = document.getElementById("type").value;
    var text = document.getElementById("textarea").value;
    var org = document.getElementById("org").value;
    var pj = document.getElementById("pj").value;
    var assignee = document.getElementById("multiSelect2").value;

    
    var container = document.getElementById(status);

    if (type === "mytask") {
        var project_show = 'none';
        var org_1 = 'My Task';
      } else {
        var project_show  = 'block';
        var org_1 = org;
      }
    
    if (priority === "High") {
        var color = 'danger'
    } else if(priority === "Medium") {
        var color = 'success'
    } else{
        var color = 'info'
    }

    if (status === "done") {
        var time_1 = 'none';
        var time_2 = 'block';
    } else {
        var time_1 = 'block';
        var time_2 = 'none';
    }

    container.innerHTML += '<!-- BEGIN: Cards -->'+
    '<div id="card-'+i+'" class="card rounded-md bg-white dark:bg-slate-800 shadow-base custom-class card-body p-6 mb-3 " style="display: block;">'+
    '  <header class="flex justify-between items-end">'+
    '    <div class="flex space-x-4 items-center rtl:space-x-reverse">'+
    '      <div class="font-medium text-base leading-6">'+
    '        <div class="dark:text-slate-200 text-slate-900 max-w-[160px] truncate">'+title+
    '        </div>'+
    '      </div>'+
    '    </div>'+
    '    <div>'+
    '      <div class="dropstart relative">'+
    '        <button class="inline-flex justify-center items-center" type="button" id="cardDropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">'+
    '          <iconify-icon class="text-xl ltr:ml-2 rtl:mr-2" icon="heroicons-outline:dots-vertical"></iconify-icon>'+
    '        </button>'+
    '        <ul class="dropdown-menu min-w-max absolute text-sm text-slate-700 dark:text-white hidden bg-white dark:bg-slate-700 shadow z-[2] float-left overflow-hidden list-none text-left rounded-lg mt-1 m-0 bg-clip-padding border-none">'+
    '          <li>'+
    '            <a href="#" data-bs-toggle="modal" data-bs-target="#editModal" class="hover:bg-slate-900 dark:hover:bg-slate-600 dark:hover:bg-opacity-70 hover:text-white w-full border-b border-b-gray-500 border-opacity-10 px-4 py-2 text-sm dark:text-slate-300 last:mb-0 cursor-pointer first:rounded-t last:rounded-b flex space-x-2 items-center capitalize rtl:space-x-reverse">'+
    '              <iconify-icon icon="clarity:note-edit-line"></iconify-icon>'+
    '              <span>View</span></a>'+
    '          </li>'+
    '          <li>'+
    '            <button name="deletetask" id="card-'+i+'-delete" class="hover:bg-slate-900 dark:hover:bg-slate-600 dark:hover:bg-opacity-70 hover:text-white w-full border-b border-b-gray-500 border-opacity-10 px-4 py-2 text-sm dark:text-slate-300 last:mb-0 cursor-pointer first:rounded-t last:rounded-b flex space-x-2 items-center capitalize rtl:space-x-reverse">'+
    '              <iconify-icon icon="fluent:delete-28-regular" class="pr-2"></iconify-icon>'+
    '              Delete</button>'+
    '          </li>'+
    '        </ul>'+
    '      </div>'+
    '    </div>'+
    '  </header>'+
    '  <div class="flex justify-between items-end"> '+
    '<div class="text-xs flex space-x-4 items-center rtl:space-x-reverse" style="display: '+project_show+';" >	'+pj+' </div>'+
    '<div class="text-xs flex space-x-4 items-center rtl:space-x-reverse" >	'+org_1+' </div>'+
    '</div> '+
    '  <div class="flex space-x-4 rtl:space-x-reverse py-3">'+
    '    <div>'+
    '      <span class="block date-label">End date</span>'+
    '      <span class="block date-text">'+date+'</span>'+
    '    </div>'+
    '  </div>'+
    '  <div id="card-'+i+'-score" style="display: '+time_2+';">'+
    '    <div class="py-1 flex">'+
    '      <div class="block date-text pr-2" style="margin-top: -4px;">Score</div>'+
    '      <div class="w-full bg-slate-200 h-2 rounded-xl overflow-hidden">'+
    '        <div class="bg-primary-500 h-full rounded-xl" style="width: 0%"></div>'+
    '      </div>'+
    '    </div>'+
    '  </div>'+
    '  <div class="ltr:text-right rtl:text-left">'+
    '    <div id="card-'+i+'-dayleft" style="display: '+time_1+';">'+
    '      <span class="rtl:text-left inline-flex items-center space-x-1 bg-'+color+'-500 bg-opacity-[0.16] text-'+color+'-500 text-xs font-normal px-2 py-1 rounded-full rtl:space-x-reverse">'+
    '        <span id="card-'+i+'-priority">'+priority+'</span>'+
    '      </span>'+
    '      <div class="inline-flex items-center space-x-1 bg-danger-500 bg-opacity-[0.16] text-danger-500 text-xs font-normal px-2 py-1 rounded-full rtl:space-x-reverse">'+
    '        <span>'+
    '          <iconify-icon icon="heroicons-outline:clipboard-list"></iconify-icon>'+
    '        </span>'+
    '        <div>'+
    '          <span>1</span>'+
    '          <span>day left</span>'+
    '        </div>'+
    '      </div>'+
    '    </div>'+
    '    <div id="card-'+i+'-done" style="display: '+time_2+';">'+
    '      <span class="rtl:text-left inline-flex items-center space-x-1 bg-'+color+'-500 bg-opacity-[0.16] text-'+color+'-500 text-xs font-normal px-2 py-1 rounded-full rtl:space-x-reverse">'+
    '        <span>'+priority+'</span>'+
    '      </span>'+
    '      <div class="inline-flex items-center space-x-1 bg-success-500 bg-opacity-[0.16] text-success-500 text-xs font-normal px-2 py-1 rounded-full rtl:space-x-reverse">'+
    '        <span>Done</span>'+
    '      </div>'+
    '    </div>'+
    '  </div>'+
    '</div>'+
    '<!-- END: Cards -->';
    buttons = document.getElementsByName("deletetask");

    const buttonPressed = e => {
        const id = e.target.id;
        const modifiedId = id.replace("-delete", "");
        const divToRemove = document.getElementById(modifiedId);
        if (divToRemove) {
            divToRemove.remove();
    }
      }
      
    for (let button of buttons) {
        button.addEventListener("click", buttonPressed);
    }

});



document.getElementById("addTaskBtnFilter").addEventListener("click", function(event) {
    event.preventDefault(); // Ngăn chặn hành vi mặc định của nút submit
    var day = document.getElementById("day").value;
    var priority = document.getElementById("Priority-filter").value;
    var type = document.getElementById("Task_haha").value;
    var org = document.getElementById("org-filter").value;

    function changeDate(innerVariable) {
        // Thực hiện xử lý với biến được truyền vào
        var result = innerVariable.substring(6, 10) + '-' + innerVariable.substring(3, 5) + '-' + innerVariable.substring(0, 2);
        return result;
      }
      function number_day_cal(k) {
        const today = new Date(); // Ngày hiện tại
            // Tạo đối tượng Date từ chuỗi ngày tháng năm
        const due_date = new Date(k);

        // Chuyển đổi thành số mili giây
        const todayMilliseconds = today.getTime();
        const dueDateMilliseconds = due_date.getTime();

        // Tính số mili giây chênh lệch
        const diffMilliseconds = dueDateMilliseconds - todayMilliseconds;

        // Chuyển đổi thành số ngày
        const diffDays = Math.ceil(diffMilliseconds / (1000 * 60 * 60 * 24));

        return diffDays;
      }
    for(var j = 1; j <= i; j++){
        var name = 'card-'+j;
        const element = document.getElementById(name);
        element.style.display = 'block';
        if (priority !== "All") {
            const element_p = document.getElementById(name+'-priority');
            const textContent_p = element_p.textContent;
            if (textContent_p !== priority){
                element.style.display = 'none';
            }
        }
        if (day !== "All") {
            const today = new Date();
            
            const element_d = document.getElementById(name+'-date');
            const textContent_d = element_d.textContent;
            var number_day = number_day_cal(changeDate(textContent_d));
            if (day === "Day"){
                if (number_day > 1){
                    element.style.display = 'none';
                }
            }
            else if(day === "Week")
                if (number_day > 8){
                element.style.display = 'none';
            }
            else if(day === "Month")
                if (number_day > 31){
                element.style.display = 'none';
            }
            else if(day === "Quarter")
                if (number_day > 92){
                element.style.display = 'none';
            }
            else if(day === "Years")
                if (number_day > 366){
                element.style.display = 'none';
            }
        }
        if (type !== "All") {

            const element_t = document.getElementById(name+'-com');
            const textContent_t = element_t.textContent;

            if (type === "My Task"){
                if (textContent_t !== "My Task"){
                    element.style.display = 'none';
            }
            }
            else{
                if (org === "All"){
                    if (textContent_t === "My Task"){
                        element.style.display = 'none';
                }}
                else if (org === "HUST")
                    if (textContent_t !== "HUST"){
                    element.style.display = 'none';
                }
                else if(org === "FPT")
                    if (textContent_t !== "FPT"){
                    element.style.display = 'none';
                }
                else if(org === "Riot Game")
                    if (textContent_t !== "Riot Game"){
                    element.style.display = 'none';
                }
            }
        }
        }
    }
  
);



const buttonPressed = e => {
    const id = e.target.id;
    const modifiedId = id.replace("-delete", "");
    const divToRemove = document.getElementById(modifiedId);
    if (divToRemove) {
        divToRemove.remove();
}
  }
  
for (let button of buttons) {
    button.addEventListener("click", buttonPressed);
}


