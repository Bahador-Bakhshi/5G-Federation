graph [
  node [
    id 0
    label 1
    disk 8
    cpu 4
    memory 14
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 3
    memory 11
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 2
    memory 7
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 1
    memory 10
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 2
    memory 14
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 2
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 50
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 195
  ]
  edge [
    source 1
    target 2
    delay 26
    bw 163
  ]
  edge [
    source 1
    target 3
    delay 27
    bw 64
  ]
  edge [
    source 1
    target 4
    delay 25
    bw 114
  ]
  edge [
    source 2
    target 5
    delay 34
    bw 124
  ]
]
