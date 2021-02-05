graph [
  node [
    id 0
    label 1
    disk 3
    cpu 2
    memory 15
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 2
    memory 10
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 3
    memory 12
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 3
    memory 9
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 4
    memory 7
  ]
  node [
    id 5
    label 6
    disk 9
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
    delay 33
    bw 109
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 160
  ]
  edge [
    source 0
    target 2
    delay 34
    bw 62
  ]
  edge [
    source 0
    target 3
    delay 32
    bw 128
  ]
  edge [
    source 1
    target 5
    delay 26
    bw 148
  ]
  edge [
    source 2
    target 4
    delay 31
    bw 119
  ]
]
