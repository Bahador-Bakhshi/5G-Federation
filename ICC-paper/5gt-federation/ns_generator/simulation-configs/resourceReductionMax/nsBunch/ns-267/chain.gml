graph [
  node [
    id 0
    label 1
    disk 9
    cpu 4
    memory 16
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 4
    memory 5
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 3
    memory 1
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 1
    memory 13
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 1
    memory 10
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 2
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 60
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 122
  ]
  edge [
    source 1
    target 2
    delay 28
    bw 96
  ]
  edge [
    source 2
    target 3
    delay 27
    bw 157
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 101
  ]
  edge [
    source 3
    target 5
    delay 28
    bw 107
  ]
]
