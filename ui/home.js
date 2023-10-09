const home = {
  template: `
<div class="centered-window">

  <button
    type="button"
    class="btn btn-primary m-2 fload-end"
    data-bs-toggle="modal"
    data-bs-target="#exampleModal"
    @click="startClick()"
  >
    Start
  </button>

  <button
    type="button"
    class="btn btn-primary m-2 fload-end"
    data-bs-toggle="modal"
    data-bs-target="#exampleModal3"
  >
    Enter Custom Ip
  </button>

  <button
    type="button"
    class="btn btn-primary m-2 fload-end"
    data-bs-toggle="modal"
    data-bs-target="#exampleModal2"
  >
    View Attendance
  </button>


  <div class="modal fade" id="exampleModal3" tabindex="-1"
    aria-labelledby="exampleModalLabel3" aria-hidden="true">

    <div class="modal-dialog modal-lg modal-dialog-centered">

      <div class="modal-content">

        <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">IP CAM</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal"
            aria-label="Close" @click=stopClick()></button>
        </div>

        <div class="modal-body">
          <div class="d-flex flex-column bd-highlight mb-3">
            <div class="p-2 w-50 bd-highlight">
              <div class="input-group">
                  <span class="input-group-text">IP</span>
                  <input type="text" id = "f1" class ="form-control" v-model="IP">
                  <button 
                    type="button" 
                    class="btn btn-primary"
                    @click=startIPClick()>
                  Confirm
                  </button>
              </div>
            </div>
            <div>
              <template v-if="flag2==1"> 
                <img :src="VideoFilePath" class="rounded mx-auto d-block" alt="Centered Image" />
              </template>
            </div>
          </div>
        </div>
      </div>          
    </div>
  </div>
  



  <div class="modal fade" id="exampleModal2" tabindex="-1"
    aria-labelledby="exampleModalLabel2" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Attendance Records</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal"
          aria-label="Close"></button>
        </div>
        <div class="modal-body">
        <table class="table table-striped">
          <thead>
            <tr>
              <th>Employee Name</th>
              <th>Time of arrival</th>
              <th>Date</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="rec in attendance">
              <td>{{rec.EmployeeName}}</td>
              <td>{{rec.EmployeeTime}}</td>
              <td>{{rec.EmployeeDate}}</td>
              <td>
                <button
                type="button"
                @click="deleteClick(rec.id)"
                class="btn btn-light mr-1"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
                          <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                  </svg>
                </button>
              </td>
              
            </tr>

          </tbody>
        </table>
        </div>
      </div>  
    </div>
  </div>

  <div class="modal fade" id="exampleModal" tabindex="-1"
    aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Live Feed</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal"
          aria-label="Close" @click="stopClick()"></button>
        </div>
        <div class="modal-body">
          <template v-if="flag==1"> 
            <img :src="VideoFilePath" class="rounded mx-auto d-block" alt="Centered Image" />
          </template>
        </div>
      </div>
    </div>
  </div>
  
</div>
`,
  data() {
    return {
      VideoFilePath: variables.VIDEO_URL,
      flag: 0,
      flag2: 0,
      attendance: [],
      IP: "",
    };
  },
  methods: {
    refreshData() {
      axios.get(variables.API_URL + "attendance").then((response) => {
        this.attendance = response.data;
      });
    },
    startClick() {
      this.VideoFilePath = variables.VIDEO_URL;
      this.VideoFilePath = this.VideoFilePath + "/start";
      this.flag = 1;
    },
    stopClick() {
      this.VideoFilePath = variables.VIDEO_URL;
      this.VideoFilePath = this.VideoFilePath + "/end";
    },
    deleteClick(id) {
      axios.delete(variables.API_URL + "attendance/" + id).then((response) => {
        alert(id);
        this.refreshData();
      });
    },
    startIPClick() {
      if (this.IP != "") {
        this.VideoFilePath = variables.VIDEO_URL;
        this.VideoFilePath = this.VideoFilePath + "/start";
        this.VideoFilePath = this.VideoFilePath + "/ip";
        axios.post(this.VideoFilePath, { IP: this.IP }).then((response) => {
          alert(response.data);
        });
      } else {
        alert("Please enter an IP address");
      }

      this.flag2 = 1;
      // alert(this.IP);
    },
  },
  mounted() {
    this.refreshData();
  },
};
