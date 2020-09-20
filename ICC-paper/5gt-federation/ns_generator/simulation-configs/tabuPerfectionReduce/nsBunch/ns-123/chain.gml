graph [
  node [
    id 0
    label 1
    disk 4
    cpu 4
    memory 13
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 2
    memory 2
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 3
    memory 11
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 3
    memory 13
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 3
    memory 2
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 2
    memory 16
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 67
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 193
  ]
  edge [
    source 0
    target 2
    delay 33
    bw 153
  ]
  edge [
    source 1
    target 3
    delay 30
    bw 116
  ]
  edge [
    source 2
    target 4
    delay 27
    bw 108
  ]
  edge [
    source 4
    target 5
    delay 33
    bw 135
  ]
]
