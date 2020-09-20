graph [
  node [
    id 0
    label 1
    disk 5
    cpu 1
    memory 5
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 1
    memory 7
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 2
    memory 15
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 4
    memory 15
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 1
    memory 6
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 1
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 142
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 68
  ]
  edge [
    source 1
    target 2
    delay 25
    bw 103
  ]
  edge [
    source 2
    target 3
    delay 29
    bw 122
  ]
  edge [
    source 3
    target 4
    delay 25
    bw 91
  ]
  edge [
    source 4
    target 5
    delay 35
    bw 79
  ]
]
