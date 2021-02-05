graph [
  node [
    id 0
    label 1
    disk 9
    cpu 4
    memory 10
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 1
    memory 11
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 1
    memory 16
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 4
    memory 14
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 4
    memory 9
  ]
  node [
    id 5
    label 6
    disk 10
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
    delay 26
    bw 74
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 73
  ]
  edge [
    source 1
    target 2
    delay 34
    bw 61
  ]
  edge [
    source 2
    target 3
    delay 30
    bw 98
  ]
  edge [
    source 2
    target 4
    delay 25
    bw 151
  ]
  edge [
    source 3
    target 5
    delay 25
    bw 122
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 54
  ]
]
