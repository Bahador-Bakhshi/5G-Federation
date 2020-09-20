graph [
  node [
    id 0
    label 1
    disk 3
    cpu 4
    memory 16
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 4
    memory 8
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 1
    memory 16
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 2
    memory 3
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 1
    memory 8
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 2
    memory 9
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 28
    bw 118
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 150
  ]
  edge [
    source 1
    target 2
    delay 27
    bw 92
  ]
  edge [
    source 1
    target 3
    delay 31
    bw 69
  ]
  edge [
    source 1
    target 4
    delay 29
    bw 116
  ]
  edge [
    source 3
    target 5
    delay 27
    bw 79
  ]
]
