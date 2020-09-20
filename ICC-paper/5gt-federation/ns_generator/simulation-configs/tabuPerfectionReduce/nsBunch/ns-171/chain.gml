graph [
  node [
    id 0
    label 1
    disk 10
    cpu 1
    memory 7
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 4
    memory 7
  ]
  node [
    id 2
    label 3
    disk 4
    cpu 3
    memory 5
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 4
    memory 9
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 1
    memory 3
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 2
    memory 5
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 87
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 73
  ]
  edge [
    source 1
    target 2
    delay 28
    bw 150
  ]
  edge [
    source 2
    target 3
    delay 25
    bw 75
  ]
  edge [
    source 2
    target 4
    delay 27
    bw 117
  ]
  edge [
    source 4
    target 5
    delay 25
    bw 162
  ]
]
