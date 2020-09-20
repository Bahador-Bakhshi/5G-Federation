graph [
  node [
    id 0
    label 1
    disk 2
    cpu 1
    memory 5
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 2
    memory 13
  ]
  node [
    id 2
    label 3
    disk 1
    cpu 2
    memory 10
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 3
    memory 10
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 4
    memory 4
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 3
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 105
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 138
  ]
  edge [
    source 1
    target 2
    delay 29
    bw 99
  ]
  edge [
    source 2
    target 3
    delay 34
    bw 194
  ]
  edge [
    source 2
    target 4
    delay 28
    bw 110
  ]
  edge [
    source 2
    target 5
    delay 25
    bw 82
  ]
]
