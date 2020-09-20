graph [
  node [
    id 0
    label 1
    disk 4
    cpu 1
    memory 13
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 1
    memory 6
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 3
    memory 11
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 4
    memory 14
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 1
    memory 15
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 3
    memory 7
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 77
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 142
  ]
  edge [
    source 0
    target 2
    delay 29
    bw 95
  ]
  edge [
    source 1
    target 3
    delay 28
    bw 200
  ]
  edge [
    source 2
    target 4
    delay 28
    bw 165
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 117
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 105
  ]
]
