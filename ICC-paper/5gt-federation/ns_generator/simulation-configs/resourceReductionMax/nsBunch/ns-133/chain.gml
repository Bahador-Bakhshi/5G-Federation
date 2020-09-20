graph [
  node [
    id 0
    label 1
    disk 6
    cpu 4
    memory 1
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 3
    memory 8
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 4
    memory 11
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 1
    memory 6
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 2
    memory 7
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 1
    memory 9
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 122
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 127
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 68
  ]
  edge [
    source 0
    target 3
    delay 35
    bw 57
  ]
  edge [
    source 1
    target 4
    delay 27
    bw 68
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 96
  ]
]
