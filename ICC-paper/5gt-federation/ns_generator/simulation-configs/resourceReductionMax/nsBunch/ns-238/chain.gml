graph [
  node [
    id 0
    label 1
    disk 2
    cpu 4
    memory 15
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 3
    memory 6
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 1
    memory 10
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 1
    memory 7
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 3
    memory 2
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 1
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 149
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 69
  ]
  edge [
    source 1
    target 2
    delay 35
    bw 84
  ]
  edge [
    source 1
    target 3
    delay 35
    bw 104
  ]
  edge [
    source 1
    target 4
    delay 26
    bw 124
  ]
  edge [
    source 2
    target 5
    delay 28
    bw 70
  ]
  edge [
    source 3
    target 5
    delay 25
    bw 98
  ]
  edge [
    source 4
    target 5
    delay 33
    bw 183
  ]
]
