graph [
  node [
    id 0
    label 1
    disk 9
    cpu 3
    memory 13
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 2
    memory 8
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 1
    memory 12
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 4
    memory 14
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 2
    memory 7
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 3
    memory 1
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 145
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
    delay 27
    bw 52
  ]
  edge [
    source 1
    target 3
    delay 28
    bw 154
  ]
  edge [
    source 1
    target 4
    delay 25
    bw 65
  ]
  edge [
    source 3
    target 5
    delay 34
    bw 59
  ]
]
