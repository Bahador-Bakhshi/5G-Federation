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
    disk 6
    cpu 2
    memory 7
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 3
    memory 1
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 2
    memory 4
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 4
    memory 2
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 3
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 112
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 120
  ]
  edge [
    source 0
    target 2
    delay 25
    bw 93
  ]
  edge [
    source 0
    target 3
    delay 27
    bw 88
  ]
  edge [
    source 2
    target 4
    delay 33
    bw 76
  ]
  edge [
    source 3
    target 5
    delay 27
    bw 142
  ]
]
