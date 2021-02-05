graph [
  node [
    id 0
    label 1
    disk 5
    cpu 3
    memory 16
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 2
    memory 4
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 2
    memory 8
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 1
    memory 4
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 4
    memory 10
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 3
    memory 9
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 157
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 77
  ]
  edge [
    source 0
    target 2
    delay 32
    bw 160
  ]
  edge [
    source 1
    target 3
    delay 25
    bw 138
  ]
  edge [
    source 2
    target 3
    delay 30
    bw 136
  ]
  edge [
    source 3
    target 4
    delay 31
    bw 196
  ]
  edge [
    source 4
    target 5
    delay 35
    bw 72
  ]
]
