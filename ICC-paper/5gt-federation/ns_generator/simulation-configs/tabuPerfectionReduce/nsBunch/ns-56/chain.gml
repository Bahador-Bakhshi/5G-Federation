graph [
  node [
    id 0
    label 1
    disk 8
    cpu 4
    memory 7
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 3
    memory 1
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 1
    memory 16
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 2
    memory 10
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 4
    memory 11
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 1
    memory 3
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 136
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 199
  ]
  edge [
    source 1
    target 2
    delay 33
    bw 134
  ]
  edge [
    source 2
    target 3
    delay 32
    bw 68
  ]
  edge [
    source 2
    target 4
    delay 33
    bw 131
  ]
  edge [
    source 2
    target 5
    delay 30
    bw 153
  ]
]
