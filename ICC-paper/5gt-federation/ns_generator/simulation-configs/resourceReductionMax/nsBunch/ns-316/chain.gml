graph [
  node [
    id 0
    label 1
    disk 10
    cpu 3
    memory 1
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 4
    memory 15
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
    disk 8
    cpu 1
    memory 11
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 3
    memory 6
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 3
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 161
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 154
  ]
  edge [
    source 1
    target 2
    delay 27
    bw 99
  ]
  edge [
    source 1
    target 3
    delay 26
    bw 155
  ]
  edge [
    source 1
    target 4
    delay 34
    bw 151
  ]
  edge [
    source 3
    target 5
    delay 30
    bw 88
  ]
]
