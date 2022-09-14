<template>
  <v-app>
    <v-content>
      <v-container fluid class="wrapper">
        <div>
          <h1 class="headline mb-0 text-md-center">DASHBOARD</h1>
        </div>
        <v-row>
          <v-col>
            
            <div class="list">
              <div>
                <h2 class="headline mb-0 text-md-center">NEW</h2>
              </div>
              <div v-for="item in tasksNew" 
                :data="item" 
                class="item" 
                :key="item.title"
                draggable
                @dragstart="startDrag($event, item)"
                @drop="onDrop($event, 1)"
                @dragover.prevent
                @dragenter.prevent>
                <v-card-title  primary-title>
                  <div>
                    <h3 class="headline mb-0">{{item.title}}</h3>
                  </div>
                </v-card-title>
              </div>
            </div>
          </v-col>
          <v-col>
            <div class="list">
              <div>
                <h2 class="headline mb-0 text-md-center">IN PROGRESS</h2>
              </div>
              <div v-for="item in tasksInProgress" 
                :data="item" 
                class="item" 
                :key="item.title"
                draggable
                @dragstart="startDrag($event, item)"
                @drop="onDrop($event, 2)"
                @dragover.prevent
                @dragenter.prevent>
                <v-card-title  primary-title>
                  <div>
                    <h3 class="headline mb-0">{{item.title}}</h3>
                  </div>
                </v-card-title>
              </div>
            </div>
          </v-col>
          <v-col>
            <div class="list">
              <div>
                <h2 class="headline mb-0 text-md-center">DONE</h2>
              </div>
              <div v-for="item in tasksDone" 
                :data="item" 
                class="item" 
                :key="item.title"
                draggable
                @dragstart="startDrag($event, item)"
                @drop="onDrop($event, 3)"
                @dragover.prevent
                @dragenter.prevent>
                  <v-card-title  primary-title>
                    <div>
                      <h3 class="headline mb-0">{{item.title}}</h3>
                    </div>
                  </v-card-title>
              </div>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script lang="ts">

export default {
  name: "App",
  components: {
  },
  data: function() {
    return {
      tasks : [
        { id: 1, title: 'Task 1', list: 1, },
        { id: 2, title: 'Task 2', list: 1, },
        { id: 3, title: 'Task 3', list: 1, },
        { id: 4, title: 'Task 4', list: 1, },
        { id: 5, title: 'Task 5', list: 1, },
        
        { id: 6, title: 'Task A', list: 2, },
        { id: 7, title: 'Task B', list: 2, },
        { id: 8, title: 'Task C', list: 2, },
        { id: 9, title: 'Task D', list: 2, },
        { id: 10, title: 'Task E', list: 2, },
        
        { id: 11, title: 'Task I', list: 3, },
        { id: 12, title: 'Task II', list: 3, },
        { id: 13, title: 'Task III', list: 3, },
        { id: 14, title: 'Task IV', list: 3, },
        { id: 15, title: 'Task V', list: 3, },
      ]
    }
  },
  computed: {
    tasksNew() {
      return this.tasks.filter((item) => item.list === 1)
    },
    tasksInProgress() {
      return this.tasks.filter((item) => item.list === 2)
    },
    tasksDone() {
      return this.tasks.filter((item) => item.list === 3)
    },},
  methods: {
    startDrag(evt, item) {
      evt.dataTransfer.dropEffect = 'move'
      evt.dataTransfer.effectAllowed = 'move'
      evt.dataTransfer.setData('itemID', item.id)
    },
    onDrop(evt, list) {
      const itemID = evt.dataTransfer.getData('itemID')
      const item = this.tasks.find((item) => item.id == itemID)
      item.list = list
    },
  }
};
</script>

<style lang="scss">
html,
body,
#app,
.v-application--wrap,
.v-content,
.v-content__wrap {
  height: 100%;
}

.drop-in {
  box-shadow: 0 0 10px rgba(0, 0, 255, 0.3);
}
</style>

<style scoped lang="scss">
.wrapper {
  .list {
    border: 1px solid black;
    margin: 100px auto;
    width: 300px;

    .item {
      padding: 20px;
      margin: 10px;
      background-color: rgb(220, 220, 255);
      display: flex;
      align-items: center;
      justify-content: center;

      &.feedback {
        background-color: rgb(255, 220, 220);
        border: 2px dashed black;
      }

      &.drag-image {
        background-color: rgb(220, 255, 220);
        transform: translate(-50%, -50%);
      }
    }
  }
}
</style>
