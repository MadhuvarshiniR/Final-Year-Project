$(document).ready(function () {

});



function display_feedback(Feedback)
{   
    let feedback = JSON.parse(Feedback)
    if (feedback['type']==0)
    {
        let card = `<div id="action-item">
        <div id="5487">
            <div class="card mb-3 bg-success text-white border-0">
                <div class="card-body p-3">
                    <div>
                        <a class="float-right text-white" href="#" role="button"
                            id="dropdownMenuLink" data-toggle="dropdown" aria-expanded="false">
                            <i class="fa fa-ellipsis-v" aria-hidden="true"></i>
                        </a>
                        <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                            <a class="dropdown-item" href="#">Action</a>
                            <a class="dropdown-item" href="#">Another action</a>
                            <a class="dropdown-item" href="#">Something else here</a>
                        </div>
                    </div>
                    <p class="card-text">`+feedback['feedback']+`
                </div>
                <div class="d-flex flex-row justify-content-end mr-2 mb-2">
                    <a class="p-2 text-white" onclick="likeCounter(this)">
                        <i class="fa fa-thumbs-up" aria-hidden="true"></i>
                        <span class="badge badge-secondary">`+feedback['likes']+`</span>
                    </a>
                    <a class="p-2 text-white" data-toggle="collapse" href="#collapseExample">
                        <i class="fa fa-comment" aria-hidden="true"></i>
                        <span class="badge badge-secondary">`+feedback['comments'].length+`</span>
                    </a>
                </div>
            </div>
            <div class="collapse" id="collapseExample">
            <!-- Comments Card -->
            `+feedback['comments'].forEach(function(item,index,array) {
                return `<div class="card card-body text-dark border-bottom mb-2">
                <div class="div row">
                    <div class="col-12 mb-2"><strong>Anonymous</strong></div>
                    <div class="col-12">`+item+`</div>
                </div>
            </div>`
            });+`
            <!-- End Comments Card -->
            </div>
        </div>
    </div>
    `
    document.getElementById("action_items_board").innerHTML+=card

    }
    else if (feedback['type']==1)
    {
        let card = `<div id="to-improve">

        <div id="5484887">
    
            <div class="card mb-3 bg-danger text-white border-0">
    
                <div class="card-body p-3">
                    <div>
                        <a class="float-right text-white" href="#" role="button"
                            id="dropdownMenuLink" data-toggle="dropdown" aria-expanded="false">
                            <i class="fa fa-ellipsis-v" aria-hidden="true"></i>
                        </a>
                        <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                            <a class="dropdown-item" href="#">Action</a>
                            <a class="dropdown-item" href="#">Another action</a>
                            <a class="dropdown-item" href="#">Something else here</a>
                        </div>
                    </div>
                    <p class="card-text">`+feedback['feedback']+`</p>
                </div>
                <div class="d-flex flex-row justify-content-end mr-2 mb-2">
                    <a class="p-2 text-white" onclick="likeCounter(this)">
                        <i class="fa fa-thumbs-up" aria-hidden="true"></i>
                        <span class="badge badge-secondary">`+feedback['likes']+`</span>
                    </a>
                    <a class="p-2 text-white" data-toggle="collapse" href="#collapseExample">
                        <i class="fa fa-comment" aria-hidden="true"></i>
                        <span class="badge badge-secondary">`+feedback['comments'].length+`</span>
                    </a>
                </div>
    
            </div>
    
            <div class="collapse" id="collapseExample">
                <!-- Comments Card -->
                `+feedback['comments'].forEach(function(item,index,array) {
                    return `<div class="card card-body text-dark border-bottom mb-2">
                    <div class="div row">
                        <div class="col-12 mb-2"><strong>Anonymous</strong></div>
                        <div class="col-12">`+item+`</div>
                    </div>
                </div>`
                });+`
                <!--  B End Comments Card -->
            </div>
        </div>
    </div>`

    document.getElementById("to_improve_board").innerHTML+=card
    
    }
    else
    {
        let card = `<!--C Card Post -->
        <div id="well-done">
        
            <div id="5487">
        
                <div class="card mb-3 bg-secondary text-white border-0">
        
                    <div class="card-body p-3">
                        <div>
                            <a class="float-right text-white" href="#" role="button"
                                id="dropdownMenuLink" data-toggle="dropdown" aria-expanded="false">
                                <i class="fa fa-ellipsis-v" aria-hidden="true"></i>
                            </a>
                            <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                                <a class="dropdown-item" href="#">Action</a>
                                <a class="dropdown-item" href="#">Another action</a>
                                <a class="dropdown-item" href="#">Something else here</a>
                            </div>
                        </div>
                        <p class="card-text">`+feedback['feedback']+`</p>
                    </div>
                    <div class="d-flex flex-row justify-content-end mr-2 mb-2">
                        <a class="p-2 text-white" onclick="likeCounter(this)">
                            <i class="fa fa-thumbs-up" aria-hidden="true"></i>
                            <span class="badge badge-secondary">`+feedback['likes']+`</span>
                        </a>
                        <a class="p-2 text-white" data-toggle="collapse" href="#collapseExample">
                            <i class="fa fa-comment" aria-hidden="true"></i>
                            <span class="badge badge-secondary">`+feedback['comments'].length+`</span>
                        </a>
                    </div>
        
                </div>
        
                <div class="collapse" id="collapseExample">
                    <!-- Comments Card -->
                    `+feedback['comments'].forEach(function(item,index,array) {
                        return `<div class="card card-body text-dark border-bottom mb-2">
                        <div class="div row">
                            <div class="col-12 mb-2"><strong>Anonymous</strong></div>
                            <div class="col-12">`+item+`</div>
                        </div>
                    </div>`
                    });+`
                    <!-- End Comments Card -->
        
        
        
                </div>
            </div>
        </div>
        <!-- C End Card Post -->`
        document.getElementById("well_done_board").innerHTML+=card
    }

}

function addCardActionItems() {
    let modal = document.getElementById("action-items-add");
    modal.style.display = "";
}
function addCardToImprove() {
    let modal = document.getElementById("to-improve-add");
    modal.style.display = "";
}
function addCardWellDone() {
    let modal = document.getElementById("well-done-add");
    modal.style.display = "";
}

function dismissFeedback(id) {
    document.getElementById(id).style.display = "none";
    document.getElementById(id.slice(0,-3)+'input').value = "";
}

function addFeedbackActionItems() {

    let content = document.getElementById("action-items-input").value;
    let parentDiv = document.getElementById("action-item");
    console.log(content);
    let id = Math.random() * 100;
    let cardContent = `<div id="` + id + `">
        <div class="card mb-3 bg-success text-white border-0">
            <div class="card-body p-3">
                <div>
                    <a class="float-right text-white" href="#" role="button"
                        id="dropdownMenuLink" data-toggle="dropdown" aria-expanded="false">
                        <i class="fa fa-ellipsis-v" aria-hidden="true"></i>
                    </a>
                    <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                        <a class="dropdown-item" href="#">Action</a>
                        <a class="dropdown-item" href="#">Another action</a>
                        <a class="dropdown-item" href="#">Something else here</a>
                    </div>
                </div>
                <p class="card-text">`+ content + `</p>
            </div>
            <div class="d-flex flex-row justify-content-end mr-2 mb-2">
                <a class="p-2 text-white" onclick="likeCounter(this)">
                    <i class="fa fa-thumbs-up" aria-hidden="true"></i>
                    <span class="badge badge-secondary">`+ 0 + `</span>
                </a>
                <a class="p-2 text-white" data-toggle="collapse" href="#collapse`+ id + `">
                    <i class="fa fa-comment" aria-hidden="true"></i>
                    <span class="badge badge-secondary">`+ 0 + `</span>
                </a>
            </div>
        </div>
        <div class="collapse" id="collapse` + id + `">
            <!-- Comments Card -->
            <div class="card card-body text-dark border-bottom mb-2">
                <div class="div row">
                    <div class="col-12 mb-2"><strong>Anonymous</strong></div>
                    <div class="col-12">Some placeholder content for the collapse component.
                        This panel is hidden by default but revealed when the user activates
                        the relevant trigger.</div>
                </div>
            </div>
            <div class="card card-body text-dark border-bottom mb-2">
                <div class="div row">
                    <div class="col-12 mb-2"><strong>Anonymous</strong></div>
                    <div class="col-12">Some placeholder content for the collapse component.
                        This panel is hidden by default but revealed when the user activates
                        the relevant trigger.</div>
                </div>
            </div>
            <div class="card card-body text-dark border-bottom mb-2">
                <div class="div row">
                    <div class="col-12 mb-2"><strong>Anonymous</strong></div>
                    <div class="col-12">Some placeholder content for the collapse component.
                        This panel is hidden by default but revealed when the user activates
                        the relevant trigger.</div>
                </div>
            </div>
            <!-- End Comments Card -->
        </div>
    </div>`;

    parentDiv.innerHTML += cardContent;

    dismissFeedback('action-items-add');
}

function addFeedbackToImprove() {

    let content = document.getElementById("to-improve-input").value;
    let parentDiv = document.getElementById("to-improve");
    console.log(content);
    let id = Math.random() * 100;
    let cardContent = `<div id="` + id + `">
        <div class="card mb-3 bg-danger text-white border-0">
            <div class="card-body p-3">
                <div>
                    <a class="float-right text-white" href="#" role="button"
                        id="dropdownMenuLink" data-toggle="dropdown" aria-expanded="false">
                        <i class="fa fa-ellipsis-v" aria-hidden="true"></i>
                    </a>
                    <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                        <a class="dropdown-item" href="#">Action</a>
                        <a class="dropdown-item" href="#">Another action</a>
                        <a class="dropdown-item" href="#">Something else here</a>
                    </div>
                </div>
                <p class="card-text">`+ content + `</p>
            </div>
            <div class="d-flex flex-row justify-content-end mr-2 mb-2">
                <a class="p-2 text-white" onclick="likeCounter(this)">
                    <i class="fa fa-thumbs-up" aria-hidden="true"></i>
                    <span class="badge badge-secondary">`+ 0 + `</span>
                </a>
                <a class="p-2 text-white" data-toggle="collapse" href="#collapse`+ id + `">
                    <i class="fa fa-comment" aria-hidden="true"></i>
                    <span class="badge badge-secondary">`+ 0 + `</span>
                </a>
            </div>
        </div>
        <div class="collapse" id="collapse` + id + `">
            <!-- Comments Card -->
            <div class="card card-body text-dark border-bottom mb-2">
                <div class="div row">
                    <div class="col-12 mb-2"><strong>Anonymous</strong></div>
                    <div class="col-12">Some placeholder content for the collapse component.
                        This panel is hidden by default but revealed when the user activates
                        the relevant trigger.</div>
                </div>
            </div>
            <div class="card card-body text-dark border-bottom mb-2">
                <div class="div row">
                    <div class="col-12 mb-2"><strong>Anonymous</strong></div>
                    <div class="col-12">Some placeholder content for the collapse component.
                        This panel is hidden by default but revealed when the user activates
                        the relevant trigger.</div>
                </div>
            </div>
            <div class="card card-body text-dark border-bottom mb-2">
                <div class="div row">
                    <div class="col-12 mb-2"><strong>Anonymous</strong></div>
                    <div class="col-12">Some placeholder content for the collapse component.
                        This panel is hidden by default but revealed when the user activates
                        the relevant trigger.</div>
                </div>
            </div>
            <!-- End Comments Card -->
        </div>
    </div>`;

    parentDiv.innerHTML += cardContent;


    dismissFeedback("to-improve-add");
}

function addFeedbackWellDone() {

    let content = document.getElementById("well-done-input").value;
    let parentDiv = document.getElementById("well-done");
    console.log(content);
    let id = Math.random() * 100;
    let cardContent = `<div id="` + id + `">
        <div class="card mb-3 bg-secondary text-white border-0">
            <div class="card-body p-3">
                <div>
                    <a class="float-right text-white" href="#" role="button"
                        id="dropdownMenuLink" data-toggle="dropdown" aria-expanded="false">
                        <i class="fa fa-ellipsis-v" aria-hidden="true"></i>
                    </a>
                    <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                        <a class="dropdown-item" href="#">Action</a>
                        <a class="dropdown-item" href="#">Another action</a>
                        <a class="dropdown-item" href="#">Something else here</a>
                    </div>
                </div>
                <p class="card-text">`+ content + `</p>
            </div>
            <div class="d-flex flex-row justify-content-end mr-2 mb-2">
                <a class="p-2 text-white" onclick="likeCounter(this)">
                    <i class="fa fa-thumbs-up" aria-hidden="true"></i>
                    <span class="badge badge-secondary">`+ 0 + `</span>
                </a>
                <a class="p-2 text-white" data-toggle="collapse" href="#collapse`+ id + `">
                    <i class="fa fa-comment" aria-hidden="true"></i>
                    <span class="badge badge-secondary">`+ 0 + `</span>
                </a>
            </div>
        </div>
        <div class="collapse" id="collapse` + id + `">
            <!-- Comments Card -->
            <div class="card card-body text-dark border-bottom mb-2">
                <div class="div row">
                    <div class="col-12 mb-2"><strong>Anonymous</strong></div>
                    <div class="col-12">Some placeholder content for the collapse component.
                        This panel is hidden by default but revealed when the user activates
                        the relevant trigger.</div>
                </div>
            </div>
            <div class="card card-body text-dark border-bottom mb-2">
                <div class="div row">
                    <div class="col-12 mb-2"><strong>Anonymous</strong></div>
                    <div class="col-12">Some placeholder content for the collapse component.
                        This panel is hidden by default but revealed when the user activates
                        the relevant trigger.</div>
                </div>
            </div>
            <div class="card card-body text-dark border-bottom mb-2">
                <div class="div row">
                    <div class="col-12 mb-2"><strong>Anonymous</strong></div>
                    <div class="col-12">Some placeholder content for the collapse component.
                        This panel is hidden by default but revealed when the user activates
                        the relevant trigger.</div>
                </div>
            </div>
            <!-- End Comments Card -->
        </div>
    </div>`;

    parentDiv.innerHTML += cardContent;


    dismissFeedback('well-done-add');
}



