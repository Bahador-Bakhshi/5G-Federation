graph [
  node [
    id 0
    label 1
    disk 9
    cpu 1
    memory 8
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 2
    memory 6
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 4
    memory 6
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 3
    memory 8
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 2
    memory 10
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 4
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
    bw 59
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 143
  ]
  edge [
    source 1
    target 2
    delay 30
    bw 64
  ]
  edge [
    source 2
    target 3
    delay 34
    bw 136
  ]
  edge [
    source 2
    target 4
    delay 28
    bw 125
  ]
  edge [
    source 4
    target 5
    delay 32
    bw 194
  ]
]
