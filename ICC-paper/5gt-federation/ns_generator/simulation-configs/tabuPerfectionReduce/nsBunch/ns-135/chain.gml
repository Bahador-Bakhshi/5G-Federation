graph [
  node [
    id 0
    label 1
    disk 6
    cpu 4
    memory 8
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 4
    memory 6
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 1
    memory 8
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 3
    memory 11
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 3
    memory 4
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 1
    memory 13
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 136
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 57
  ]
  edge [
    source 1
    target 2
    delay 28
    bw 59
  ]
  edge [
    source 2
    target 3
    delay 31
    bw 70
  ]
  edge [
    source 2
    target 4
    delay 25
    bw 185
  ]
  edge [
    source 2
    target 5
    delay 32
    bw 112
  ]
]
