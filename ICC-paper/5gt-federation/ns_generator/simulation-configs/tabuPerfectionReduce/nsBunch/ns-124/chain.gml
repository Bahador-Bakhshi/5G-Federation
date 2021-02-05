graph [
  node [
    id 0
    label 1
    disk 9
    cpu 4
    memory 14
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 1
    memory 15
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 3
    memory 5
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 3
    memory 16
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 1
    memory 1
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
    delay 30
    bw 68
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 56
  ]
  edge [
    source 1
    target 2
    delay 34
    bw 85
  ]
  edge [
    source 2
    target 3
    delay 25
    bw 101
  ]
  edge [
    source 2
    target 4
    delay 30
    bw 87
  ]
  edge [
    source 2
    target 5
    delay 29
    bw 98
  ]
]
