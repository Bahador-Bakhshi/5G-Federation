graph [
  node [
    id 0
    label 1
    disk 1
    cpu 2
    memory 4
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 2
    memory 8
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 1
    memory 16
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 4
    memory 7
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 1
    memory 3
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 2
    memory 13
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 136
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 190
  ]
  edge [
    source 1
    target 2
    delay 28
    bw 143
  ]
  edge [
    source 1
    target 3
    delay 32
    bw 140
  ]
  edge [
    source 2
    target 5
    delay 30
    bw 116
  ]
  edge [
    source 3
    target 4
    delay 32
    bw 143
  ]
]
