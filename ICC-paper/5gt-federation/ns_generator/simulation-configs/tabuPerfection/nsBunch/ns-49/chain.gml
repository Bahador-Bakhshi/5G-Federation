graph [
  node [
    id 0
    label 1
    disk 7
    cpu 4
    memory 8
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 4
    memory 15
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 1
    memory 6
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 3
    memory 6
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 2
    memory 13
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 2
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 72
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 91
  ]
  edge [
    source 1
    target 2
    delay 27
    bw 120
  ]
  edge [
    source 1
    target 3
    delay 33
    bw 87
  ]
  edge [
    source 1
    target 4
    delay 27
    bw 175
  ]
  edge [
    source 2
    target 5
    delay 25
    bw 111
  ]
]
