graph [
  node [
    id 0
    label 1
    disk 4
    cpu 2
    memory 7
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 1
    memory 4
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 3
    memory 16
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 1
    memory 12
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 3
    memory 8
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 3
    memory 16
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 90
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 150
  ]
  edge [
    source 1
    target 2
    delay 25
    bw 79
  ]
  edge [
    source 1
    target 3
    delay 30
    bw 89
  ]
  edge [
    source 1
    target 4
    delay 32
    bw 139
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 157
  ]
]
