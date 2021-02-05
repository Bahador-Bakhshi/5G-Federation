graph [
  node [
    id 0
    label 1
    disk 10
    cpu 4
    memory 16
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 4
    memory 13
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 3
    memory 2
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 4
    memory 10
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 1
    memory 9
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 2
    memory 2
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 106
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 71
  ]
  edge [
    source 1
    target 2
    delay 34
    bw 133
  ]
  edge [
    source 2
    target 3
    delay 25
    bw 140
  ]
  edge [
    source 2
    target 4
    delay 31
    bw 170
  ]
  edge [
    source 2
    target 5
    delay 34
    bw 92
  ]
]
